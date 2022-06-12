import braintree

from decimal import Decimal

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings

from orders.models import Order
from .tasks import payment_completed


gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        client_token: str = gateway.client_token.generate()

        return render(request, "payment/process.html", {
            "client_token": client_token,
        })

    order_id: str = request.session.get("order_id")
    order: Order = get_object_or_404(Order, id=order_id)
    total_price: Decimal = order.total_price
    nonce: str | None = request.POST.get("payment_method_nonce")

    result: bool = gateway.transaction.sale({
        "amount": f"{total_price:.2f}",
        "payment_method_nonce": nonce,
        "options": {
            "submit_for_settlement": True,
        },
    })

    if not result.is_success:
        return redirect("payment:canceled")

    order.paid = True
    order.transaction_id = result.transaction.id
    order.save()

    payment_completed.delay(order.id)

    return redirect("payment:done")


def payment_done(request: HttpRequest) -> HttpResponse:
    return render(request, "payment/done.html")


def payment_canceled(request: HttpRequest) -> HttpResponse:
    return render(request, "payment/canceled.html")
