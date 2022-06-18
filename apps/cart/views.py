from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .cart import Cart
from .forms import CartUpdateForm


@require_POST
def update_product(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)

    action: str = request.POST.get("action", "")
    quantity: int
    override = False
    size_id = int(request.POST["size_id"])

    if action == "add":
        quantity = 1
    elif action == "remove":
        quantity = -1
    else:
        quantity = int(request.POST.get("quantity"))
        override = True

    cart.add(product_id, size_id, quantity=quantity, override_qty=override)

    return redirect(request.META.get("HTTP_REFERER", "/"))


@require_POST
def remove_product(request: HttpRequest, product_id: str) -> HttpResponse:
    cart = Cart(request)
    cart.remove(product_id)

    return redirect(request.META.get("HTTP_REFERER", "/"))


@require_POST
def clear(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    cart.clear()

    return redirect(request.META.get("HTTP_REFERER", "/"))


def summary(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)

    for item in cart:
        item["update_form"] = CartUpdateForm(initial={
            "quantity": item["quantity"],
        })

    if len(cart) == 0:
        messages.error(request, "Ваша корзина пока пуста.")

    return render(request, "cart/summary.html", {
        "cart": cart,
    })
