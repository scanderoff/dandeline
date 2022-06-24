from typing import Any

from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import QuerySet, Prefetch
from django.views.decorators.http import require_GET

from apps.bookmark.services.bookmark import Bookmark
from .models import *
from .services.recommender import Recommender
from .services.catalog import Catalog


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/homepage.html", {})


def catalog(request: HttpRequest, path: str = "") -> HttpResponse:
    catalog = Catalog(path)
    products: QuerySet[Product] = catalog.get_products(catalog.descendant_cats)

    # for prod in products:
    #     if prod.name != "Белов Ян Димитриевич":
    #         continue

    #     print(prod.name, prod.sizes)
    #     print(prod.name, prod.variations.all())

    return render(request, "shop/catalog.html", {
        "path": catalog.ancestor_cats,
        "category": catalog.current_cat,
        "products": products,
        "sizes": catalog.sizes,
        "bookmark": Bookmark(request),
    })


def product(request: HttpRequest, slug: str) -> HttpResponse:
    catalog = Catalog()
    product: Product = catalog.get_product(slug)

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
