from django.conf import settings
from django.http import HttpRequest
from django.db.models import QuerySet

from src.catalog.models import Product


class Bookmark:
    @property
    def products(self) -> QuerySet[Product]:
        if self.__products is not None:
            return self.__products

        self.__products = Product.objects.filter(id__in=self.bookmark)

        return self.__products

    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        bookmark: list[int] | None = self.session.get(settings.BOOKMARK_SESSION_ID)

        if bookmark is None:
            bookmark = self.session[settings.BOOKMARK_SESSION_ID] = []

        self.bookmark = bookmark
        self.__products = None

    def add(self, product_id: int) -> None:
        if product_id not in self.bookmark:
            self.bookmark.append(product_id)
            self.save()

    def remove(self, product_id: int) -> None:
        if product_id in self.bookmark:
            self.bookmark.remove(product_id)
            self.save()

    def save(self) -> None:
        self.session.modified = True

    def clear(self) -> None:
        del self.session[settings.BOOKMARK_SESSION_ID]
        self.save()

    def __iter__(self) -> Product:
        for product in self.products:
            yield product

    def __len__(self) -> int:
        return len(self.bookmark)

    def __contains__(self, product: Product) -> bool:
        return product.id in self.bookmark
