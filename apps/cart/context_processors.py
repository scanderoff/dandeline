from typing import Any

from django.http import HttpRequest

from .cart import Cart


def cart(request: HttpRequest) -> dict[str, Any]:
    cart = Cart(request)

    return {
        "cart": cart,
    }
