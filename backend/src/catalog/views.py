import urllib.parse
from typing import Any

from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import QuerySet
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from src.utils import is_ajax
from src.bookmark.services.bookmark import Bookmark
from .models import *
# from .services.recommender import Recommender
from .forms import FilterForm
from .serializers import ProductSerializer, VariationSerializer
from .pagination import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    lookup_field = "slug"

    def get_queryset(self) -> QuerySet:
        queryset = Product.objects.all().distinct()

        query_params: dict[str, Any] = self.request.query_params
        category: str = query_params.get("category")
        price_from: str = query_params.get("price_from")
        price_to: str = query_params.get("price_to")
        sizes: list[str] = query_params.getlist("size")
        s: str = query_params.get("s")
        order_by: str = query_params.get("order_by", "-created_at")

        if category:
            cat: Category = get_object_or_404(Category, pk=category)
            descendants = cat.get_descendants(include_self=True)

            queryset = queryset.filter(category__in=descendants)

        if price_from:
            queryset = queryset.filter(price__gte=price_from)

        if price_to:
            queryset = queryset.filter(price__lte=price_to)

        if sizes:
            queryset = queryset.filter(variations__size__in=sizes)

        if s:
            queryset = queryset.filter(name__icontains=s)

        queryset = queryset.order_by(order_by)

        return queryset


class VariationListAPIView(ListAPIView):
    serializer_class = VariationSerializer

    def get_queryset(self) -> QuerySet:
        queryset = Variation.objects.all()

        query_params: dict[str, Any] = self.request.query_params
        product_id: str = query_params.get("product_id")
        size_id: str = query_params.get("size_id")
        color_id: str = query_params.get("color_id")

        queryset = Variation.objects.filter(
            product__id=product_id,
            size__id=size_id,
            color__id=color_id,
        )

        return queryset


def products(request: HttpRequest, path: str = "") -> HttpResponse:
    current_cat: Category | None = None
    descendants: list[Category] = []
    ancestors: list[Category] = []

    filter_form = FilterForm(data=request.GET or None)
    products: QuerySet[Product] = Product.objects.order_by("-created_at").distinct()

    if path:
        try:
            cats: list[str] = path.rsplit("/", 2)
            cat_slug: str = urllib.parse.unquote(cats.pop()) # tmp
            parent_slug: str = urllib.parse.unquote(cats.pop()) # tmp
        except IndexError:
            parent_slug: str = None

        current_cat: Category = get_object_or_404(Category, slug=cat_slug, parent__slug=parent_slug)

        family: list[Category] = list(current_cat.get_family())
        index: int = family.index(current_cat)

        descendants = family[index:]
        ancestors = family[:index+1]

        products = products.filter(category__in=descendants)


    if filter_form.is_valid():
        cd: dict[str, Any] = filter_form.cleaned_data

        if cd["price_from"]:
            products = products.filter(price__gte=cd["price_from"])

        if cd["price_to"]:
            products = products.filter(price__lte=cd["price_to"])

        if cd["size"]:
            products = products.filter(variations__size__in=cd["size"])

        if cd["s"]:
            products = products.filter(name__icontains=cd["s"])

        products = products.order_by(request.GET.get("order_by", "-created_at"))


    paginator = Paginator(products, 15)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        if is_ajax(request):
            return HttpResponse("")

        products = paginator.page(paginator.num_pages)

    if is_ajax(request):
        return render(request, "catalog/_product_loop.html", {
            "products": products,
        })

    return render(request, "catalog/products.html", {
        "path": path,
        "ancestors": ancestors,
        "category": current_cat,
        "products": products,
        "filter_form": filter_form,
        "bookmark": Bookmark(request),
    })


def product(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        product: Product = Product.objects.select_related("category").get(slug=slug)
    except Product.DoesNotExist:
        raise Http404()

    # Предложить продукты, которые чаще всего покупаются с этим продуктом
    # r = Recommender()
    # recommended_products: list[Product] = r.suggest_products_for([product], 4)

    return render(request, "catalog/product.html", {
        "product": product,
        # "recommended_products": recommended_products,
    })


@require_GET
def variation(request: HttpRequest) -> JsonResponse:
    data: dict[str, Any] = request.GET

    try:
        variation: Variation = Variation.objects.get(
            product__id=data["product_id"],
            size__id=data["size_id"],
            color__id=data["color_id"],
        )
    except Variation.DoesNotExist:
        return JsonResponse({"success": False})

    return JsonResponse({
        "success": True,

        "variation_id": variation.id,
    })
