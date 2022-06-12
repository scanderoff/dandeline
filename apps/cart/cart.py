from typing import Any
from decimal import Decimal

from django.conf import settings
from django.http import HttpRequest
from django.db.models import QuerySet

from coupons.models import Coupon
from shop.models import Product


class Cart:
    @property
    def total_price(self) -> Decimal:
        return sum(item["total_price"] for item in self)

    @property
    def coupon(self) -> Coupon | None:
        if self.__coupon is not None:
            return self.__coupon

        coupon_id: str = self.session.get("coupon_id")

        if coupon_id is None:
            return None

        try:
            self.__coupon = Coupon.objects.get(id=coupon_id)
        except Coupon.DoesNotExist:
            pass

        return self.__coupon

    @property
    def discount(self) -> Decimal:
        if not self.coupon:
            return Decimal(0)

        return self.coupon.discount/Decimal(100) * self.total_price

    @property
    def discounted_total_price(self) -> Decimal:
        return self.total_price - self.discount

    @property
    def products(self) -> QuerySet:
        if self.__products is not None:
            return self.__products

        product_ids = self.cart.keys()
        self.__products = Product.objects.filter(id__in=product_ids)

        return self.__products

    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart: dict[str, Any] | None = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart: dict[str, Any]
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        self.__products = None
        self.__coupon = None

    def add(self, product: Product, quantity: int = 1, override_quantity: bool = False) -> None:
        product_id: str = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                # TODO
                # "variations": {
                #     "size": None,
                #     "color": None,
                # }
            }

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    def save(self) -> None:
        self.session.modified = True

    def remove(self, product: Product) -> None:
        product_id: str = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self) -> None:
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self) -> dict[str, Any]:
        cart: dict[str, Any] = self.cart.copy()

        for product in self.products:
            product_id: str = str(product.id)

            item: Any = cart[product_id]
            item["product"] = product
            item["total_price"] = item["quantity"] * product.price

            yield item

    def __len__(self) -> int:
        return sum(item["quantity"] for item in self.cart.values())