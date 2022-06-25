from typing import Any

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from django.db.models import QuerySet
from django.views.decorators.http import require_GET

from bookmark.services.bookmark import Bookmark
from .models import *
from .services.recommender import Recommender
from .forms import FilterForm


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/homepage.html", {})


def catalog(request: HttpRequest, path: str = "") -> HttpResponse:
    current_cat: Category | None = None
    descendants: list[Category] = []
    ancestors: list[Category] = []


    filter_form = FilterForm(data=request.GET)
    products: QuerySet[Product] = Product.objects.prefetch_attributes()


    if path:
        cat_slug: str = path.rsplit("/", 1)[-1]

        current_cat: Category = get_object_or_404(Category, slug=cat_slug)

        family: list[Category] = list(current_cat.get_family())
        index: int = family.index(current_cat)

        descendants = family[index:]
        ancestors = family[:index+1]

        products = products.filter(category__in=descendants)


    if filter_form.is_valid():
        cd: dict[str, Any] = filter_form.cleaned_data

        products = products \
            .filter(price__gte=cd["price_from"]) \
            .filter(price__lte=cd["price_to"])
        print(cd)
        if cd["size"]:
            products = products.filter(variations__size__in=cd["size"])

    products = products.order_by("created_at")

    return render(request, "shop/catalog.html", {
        "path": ancestors,
        "category": current_cat,
        "products": products,
        "filter_form": filter_form,
        "bookmark": Bookmark(request),
    })


def product(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        product: Product = (
            Product.objects
                .prefetch_attributes()
                .select_related("category")
                .get(slug=slug)
        )
    except Product.DoesNotExist:
        raise Http404()

    r = Recommender()
    recommended_products: list[Product] = r.suggest_products_for([product], 4)

    return render(request, "shop/product.html", {
        "product": product,
        "recommended_products": recommended_products,
    })


@require_GET
def get_variation(request: HttpRequest) -> JsonResponse:
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
