from django.urls import URLPattern, path

from .apps import CouponsConfig
from . import views


app_name: str = CouponsConfig.name

urlpatterns: list[URLPattern] = [
    path("apply", views.coupon_apply, name="apply"),
]
