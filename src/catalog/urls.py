from django.urls import URLPattern, path

from .apps import CatalogConfig
from . import views


app_name: str = CatalogConfig.name

urlpatterns: list[URLPattern] = [
    path("get-variation", views.get_variation, name="get-variation"),

    path("", views.products, name="products"),
    path("category/<path:path>/", views.products, name="products"),

    path("product/<str:slug>/", views.product, name="product"),
]
