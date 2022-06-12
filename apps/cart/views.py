from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from shop.models import Product
from .cart import Cart
from .forms import CartUpdateForm


@require_POST
def update_product(request: HttpRequest, product_id: str) -> HttpResponse:
    cart: Cart = Cart(request)
    product: Product = get_object_or_404(Product, id=product_id)

    action: str = request.POST.get("action", "")
    quantity: int
    override: bool = False

    if action == "add":
        quantity = 1
    elif action == "remove":
        quantity = -1
    else:
        quantity = int(request.POST.get("quantity"))
        override = True

    cart.add(product, quantity=quantity, override_quantity=override)

    return redirect("cart:detail")


@require_POST
def remove_product(request: HttpRequest, product_id: str) -> HttpResponse:
    cart: Cart = Cart(request)
    product: Product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    return redirect("cart:detail")


def cart_detail(request: HttpRequest) -> HttpResponse:
    cart: Cart = Cart(request)

    for item in cart:
        item["update_form"] = CartUpdateForm(initial={
            "quantity": item["quantity"],
        })

    if len(cart) == 0:
        messages.error(request, "Ваша корзина пока пуста.")

    return render(request, "cart/detail.html", {
        "cart": cart,
    })
