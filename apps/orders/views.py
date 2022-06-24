import weasyprint

from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, HttpResponse
from django.views import View

from coupons.forms import CouponApplyForm
from .models import Order
from .forms import OrderCreateForm
from .services.checkout import CheckoutProcessor


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
        checkout_form = OrderCreateForm.from_user(request.user)
        coupon_form = CouponApplyForm(auto_id=False)

        return render(request, "orders/checkout.html", {
            "checkout_form": checkout_form,
            "coupon_form": coupon_form,
        })

    def post(self, request: HttpRequest) -> HttpResponse:
        checkout_processor = CheckoutProcessor(request)

        try:
            checkout_processor.run()
        except ValidationError:
            return render(request, "orders/checkout.html", {
                "cart": checkout_processor.cart,
                "form": checkout_processor.form,
            })

        # return redirect("payment:process")
        return redirect("users:edit")
