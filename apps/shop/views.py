from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from bookmark.bookmark import Bookmark
from .models import *
from .recommender import Recommender


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/homepage.html", {})


def catalog(request: HttpRequest, path: str = "") -> HttpResponse:
    category: Category | None = None
    ancestors: list[Category] = []
    products: QuerySet[Product] = Product.objects.all()

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
    variations: QuerySet[Variation] = (
        product.variations
            .select_related("size")
            # .select_related("color")
            .all()
    )

    r = Recommender()
    recommended_products: list[Product] = r.suggest_products_for([product], 4)

    return render(request, "shop/product.html", {
        "product": product,
        "variations": variations,
        "recommended_products": recommended_products,
    })
