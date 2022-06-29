import json
from typing import Any
from decimal import Decimal

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
# from django.template.loader import render_to_string

from coupons.forms import CouponApplyForm
from .services.cart import Cart


@require_POST
def update(request: HttpRequest) -> JsonResponse:
    cart = Cart(request)
    # data = json.loads(request.body)
    data = request.POST

    variation_id = int(data["variation_id"])
    action: str = data.get("do", "")
    override = False

    if action == "add":
        qty = 1
    elif action == "remove":
        qty = -1
    else:
        qty = int(data["quantity"])
        override = True

    cart.add(variation_id, qty=qty, override_qty=override)

    return redirect(request.META.get("HTTP_REFERER", "/"))

    # с аяксом вьюха разрастается((
    # item: dict[str, Any] = cart.get_item(variation_id)
    # item_qty: int = item["quantity"]
    # item_price: Decimal = item_qty*item["variation"].product.price
    # html = ""

    # if item_qty == 1 and action == "add":
    #     html = render_to_string("cart/_item.html", {"item": item})

    # return JsonResponse({
    #     "success": True,

    #     "variationId": variation_id,
    #     "newQty": item_qty,
    #     "itemPrice": f"{item_price:.2f}",
    #     "totalItems": len(cart),
    #     "totalPrice": cart.total_price,
    #     "html": html,
    # })


@require_POST
def remove(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    data = request.POST
    # data = json.loads(request.body)

    variation_id = int(data["variation_id"])

    cart.remove(variation_id)

    return redirect(request.META.get("HTTP_REFERER", "/"))


@require_POST
def clear(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    cart.clear()

    return redirect(request.META.get("HTTP_REFERER", "/"))


def summary(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()

    if len(cart) == 0:
        messages.error(request, "Ваша корзина пока пуста.")

    return render(request, "cart/summary.html", {
        "cart": cart,
        "coupon_apply_form": coupon_apply_form,
    })
