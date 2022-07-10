import weasyprint

from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model, login
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.db.models import Model

from cart.services.cart import Cart
from coupons.forms import CouponApplyForm
from .models import Order, OrderItem
from .forms import OrderCreateForm
# from .tasks import order_created



User: type[Model] = get_user_model()


def register_on_checkout(request: HttpRequest, order: Order) -> User:
    """Register after placing an order"""

    password: str = User.objects.make_random_password()

    user: User = User.objects.from_order(order, password)
    login(request, user)

    return user


@staff_member_required
def admin_order_pdf(_: HttpRequest, order_id: str) -> HttpResponse:
    order: Order = get_object_or_404(Order, id=order_id)
    html: str = render_to_string("orders/pdf.html", {
        "order": order,
    })

    response: HttpResponse = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_{order.id}.pdf"

    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / "styles/pdf.css")]
    )

    return response


class CheckoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        cart = Cart(request)

        if len(cart) == 0:
            return redirect("catalog:products")

        checkout_form = OrderCreateForm.from_user(request.user)
        coupon_form = CouponApplyForm(auto_id=False)

        return render(request, "orders/checkout.html", {
            "checkout_form": checkout_form,
            "coupon_form": coupon_form,
        })

    def post(self, request: HttpRequest) -> HttpResponse:
        cart = Cart(request)
        form = OrderCreateForm(request.POST)

        if not form.is_valid():
            return render(request, "orders/checkout.html", {
                "cart": cart,
                "form": form,
            })

        order = form.save(commit=False)
        user: User = request.user

        if not user.is_authenticated:
            user = register_on_checkout(request, order)

        order.user = user

        if cart.coupon:
            order.coupon = cart.coupon
            order.discount = cart.coupon.discount

        order.save()





        order_items: list[OrderItem] = []

        for item in cart:
            order_item = OrderItem(
                order=order,
                variation=item["variation"],
                quantity=item["quantity"],
            )

            order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)

        cart.clear()





        # order_created.delay(order.id)

        request.session["order_id"] = order.id



        # return redirect("payment:process")
        return redirect("users:orders")
