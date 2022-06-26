from typing import Any, Iterable
from decimal import Decimal

from django.conf import settings
from django.http import HttpRequest
from django.db.models import QuerySet

from coupons.models import Coupon
from catalog.models import Variation


class Cart:
    @property
    def total_price(self) -> Decimal:
        return sum(item["total_price"] for item in self)

    @property
    def coupon(self) -> Coupon | None:
        if self.__coupon is not None:
            return self.__coupon

        coupon_id: str | None = self.session.get("coupon_id")

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
    def variations(self) -> dict[int, Variation]:
        if self.__variations is not None:
            return self.__variations

        variation_ids: Iterable = self.cart.keys()

        self.__variations = Variation.objects \
            .filter(id__in=variation_ids) \
            .select_related("product", "size", "color") \
            .in_bulk() \

        return self.__variations

    def __init__(self, request: HttpRequest) -> None:
        self.session = request.session
        cart: dict[str, Any] | None = self.session.get(settings.CART_SESSION_ID)

        if cart is None:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        self.__variations = None
        self.__coupon = None


    def add(self, variation_id: int, qty: int = 1, override_qty: bool = False) -> None:
        variation_id = str(variation_id)
        item: dict[str, Any] | None = self.cart.get(variation_id)

        if item is None:
            item = self.cart[variation_id] = {
                "quantity": 0,
            }

        if override_qty:
            item["quantity"] = qty
        else:
            item["quantity"] += qty

        if item["quantity"] < 1:
            self.remove(variation_id)
        else:
            self.save()

    def remove(self, variation_id: int) -> None:
        variation_id = str(variation_id)

        if variation_id in self.cart:
            del self.cart[variation_id]
            self.save()

    def save(self) -> None:
        self.session.modified = True

    def clear(self) -> None:
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self) -> dict[str, Any]:
        for variation_id in self.cart:
            item: dict[str, Any] = self.get_item(int(variation_id))

            yield item

    def get_item(self, variation_id: int) -> dict[str, Any] | None:
        if variation_id not in self.variations:
            return None

        variation: Variation = self.variations[variation_id]

        item: dict[str, Any] = {**self.cart[str(variation_id)]}
        item["variation"] = variation
        item["total_price"] = item["quantity"] * variation.product.price

        return item

    def __len__(self) -> int:
        return sum(item["quantity"] for item in self.cart.values())
