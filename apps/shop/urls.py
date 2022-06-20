from django.urls import URLPattern, path

from .apps import ShopConfig
from . import views


app_name: str = ShopConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.homepage, name="homepage"),

    path("catalog/", views.catalog, name="catalog"),
    path("catalog/<path:path>/", views.catalog, name="catalog"),

    path("product/<str:slug>/", views.product, name="product"),

    path("get-variation", views.get_variation, name="get-variation"),
]
