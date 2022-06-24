from typing import Iterable

from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

from ..models import Category, Product, Size


class Catalog:
    PRODUCTS_PER_PAGE = 15

    def __init__(self, path: str = "") -> None:
        self.sizes = Size.objects.all()

        self.current_cat = None
        self.descendant_cats = None
        self.ancestor_cats = None

        if not path:
            return

        cat_slug: str = path.rsplit("/", 1)[-1]

        self.current_cat = get_object_or_404(Category, slug=cat_slug)

        branch: list[Category] = list(self.current_cat.get_family())
        index: int = branch.index(self.current_cat)

        self.descendant_cats = branch[index:]
        self.ancestor_cats = branch[:index+1]

    def get_products(self, categories: Iterable[Category] | None = None) -> QuerySet[Product]:
        products: QuerySet[Product] = Product.objects.prefetch_attributes()

        if categories is not None:
            products = products.filter(category__in=categories)

        return products[:Catalog.PRODUCTS_PER_PAGE]

    def get_product(self, slug: str) -> Product:
        try:
            product: Product = (
                Product.objects
                    .prefetch_attributes()
                    .select_related("category")
                    .get(slug=slug)
            )
        except Product.DoesNotExist:
            ...

        return product
