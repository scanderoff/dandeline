from typing import Any

from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import QuerySet, Prefetch
from django.views.decorators.http import require_GET

from bookmark.bookmark import Bookmark
from .models import *
from .recommender import Recommender


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/homepage.html", {})


def catalog(request: HttpRequest, path: str = "") -> HttpResponse:
    category: Category | None = None
    ancestors: list[Category] = []

    products: QuerySet[Product] = (
        Product.objects
            .prefetch_related(Prefetch(
                "variations",
                queryset=Variation.objects
                    .select_related("size")
                    .select_related("color")
                    .distinct("color"),
                to_attr="color_variations",
            ))
            .prefetch_related(Prefetch(
                "variations",
                queryset=Variation.objects
                    .select_related("size")
                    .select_related("color")
                    .distinct("size"),
                to_attr="size_variations",
            ))
            .all()[:15]
    )

    if path:
        category_slug: str = path.rsplit("/", 1)[-1]
        category = get_object_or_404(Category, slug=category_slug)
        branch: list[Category] = list(category.get_family())

        index: int = branch.index(category)
        descendants: list[Category] = branch[index:]
        ancestors = branch[:index+1]

        products = products.filter(category__in=descendants)[:15]

    sizes: QuerySet[Size] = Size.objects.all()

    return render(request, "shop/catalog.html", {
        "path": ancestors,
        "category": category,
        "products": products,
        "sizes": sizes,
        "bookmark": Bookmark(request),
    })


def product(request: HttpRequest, slug: str) -> HttpResponse:
    product: Product = get_object_or_404(Product, slug=slug)

    sizes: QuerySet = (
        product.variations
            .select_related("size")
            .distinct("size")
            .values("size", "size__value")
    )

    colors: QuerySet = (
        product.variations
            .select_related("color")
            .distinct("color")
            .values("color", "color__value")
    )

    r = Recommender()
    recommended_products: list[Product] = r.suggest_products_for([product], 4)

    return render(request, "shop/product.html", {
        "product": product,
        "sizes": sizes,
        "colors": colors,
        "recommended_products": recommended_products,
    })


require_GET
def get_variation(request: HttpRequest) -> JsonResponse:
    data: dict[str, Any] = request.GET

    try:
        variation: Variation = Variation.objects.get(
            product__id=data["product_id"],
            size__id=data["size_id"],
            color__id=data["color_id"],
        )
    except Variation.DoesNotExist:
        return JsonResponse({"status": "Not found"})

    return JsonResponse({
        "status": "Success",

        "variation_id": variation.id,
    })
