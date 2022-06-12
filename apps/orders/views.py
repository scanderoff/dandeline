import weasyprint

from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.views import View

from users.models import User
from coupons.forms import CouponApplyForm
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from .utils import register_on_checkout


@staff_member_required
def admin_order_pdf(request: HttpRequest, order_id: str) -> HttpResponse:
    order: Order = get_object_or_404(Order, id=order_id)
    html: str = render_to_string("orders/pdf.html", {
        "order": order,
    })

    response: HttpResponse = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_{order.id}.pdf"

    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(settings.STATICFILES_DIRS[0] / "styles/pdf.css")]
    )

    return response


class CheckoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        cart: Cart = Cart(request)
        user: User = request.user
        initial: dict[str, str] = {}

        if user.is_authenticated:
            initial["first_name"] = user.first_name
            initial["last_name"] = user.last_name
            initial["phone"] = user.phone
            initial["email"] = user.email
            initial["zip_code"] = user.zip_code
            initial["city"] = user.city
            initial["address1"] = user.address1
            initial["address2"] = user.address2

        form: OrderCreateForm = OrderCreateForm(initial=initial)
        coupon_form: CouponApplyForm = CouponApplyForm(auto_id=False)

        return render(request, "orders/checkout.html", {
            "cart": cart,
            "form": form,
            "coupon_form": coupon_form,
        })

    def post(self, request: HttpRequest) -> HttpResponse:
        cart: Cart = Cart(request)
        form: OrderCreateForm = OrderCreateForm(request.POST)

        if not form.is_valid():
            return render(request, "orders/checkout.html", {
                "cart": cart,
                "form": form,
            })

        order: Order = form.save(commit=False)
        user: User = request.user

        if not user.is_authenticated:
            user = register_on_checkout(order)
            login(request, user, "allauth.account.auth_backends.AuthenticationBackend")

        order.user = user

        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount
        order.save()

        order_items: list[OrderItem] = []

        for item in cart:
            order_item: OrderItem = OrderItem(
                order=order,
                product=item["product"],
                quantity=item["quantity"]
            )
            order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)

        cart.clear()

        order_created.delay(order.id)

        request.session["order_id"] = order.id

        return redirect(reverse("payment:process"))
