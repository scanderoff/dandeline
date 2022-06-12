from django.urls import path, URLPattern

from . import views

app_name: str = "cart"

urlpatterns: list[URLPattern] = [
    path("", views.cart_detail, name="detail"),
    # path("add-product/<int:product_id>", views.add_product, name="add_product"),
    path("remove-product/<int:product_id>", views.remove_product, name="remove-product"),
    path("update-product/<int:product_id>", views.update_product, name="update-product"),
]
