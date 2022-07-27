from django.urls import URLPattern, path

from .apps import OrdersConfig
from . import views


app_name: str = OrdersConfig.name

urlpatterns: list[URLPattern] = [
    path("admin/order/<int:order_id>/pdf", views.admin_order_pdf, name="admin_order_pdf"),
    path("checkout", views.CheckoutView.as_view(), name="checkout"),

    path("orders/", views.OrderListCreateAPIView.as_view(), name="orders"),
]
