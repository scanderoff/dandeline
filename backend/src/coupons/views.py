from datetime import datetime

from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import CouponApplyForm


@require_POST
def apply(request: HttpRequest) -> HttpResponse:
    now: datetime = timezone.now()
    form = CouponApplyForm(request.POST)

    if form.is_valid():
        code: str = form.cleaned_data["code"]

        try:
            coupon: Coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True,
            )

            request.session["coupon_id"] = coupon.id
        except Coupon.DoesNotExist:
            request.session["coupon_id"] = None

    return redirect(request.META.get("HTTP_REFERER", "/"))
