from django.urls import URLPattern, path

from .apps import PaymentConfig
from . import views


app_name: str = PaymentConfig.name

urlpatterns: list[URLPattern] = [
    path("process", views.payment_process, name="process"),
    path("done", views.payment_done, name="done"),
    path("canceled", views.payment_canceled, name="canceled"),
]

