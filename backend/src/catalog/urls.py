from django.urls import URLPattern, path, include
from rest_framework import routers

from .apps import CatalogConfig
from .views import variation, products, product, ProductViewSet, VariationListAPIView


app_name: str = CatalogConfig.name
router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")


urlpatterns: list[URLPattern] = [
    path("variation", variation, name="variation"),

    path("", products, name="products"),
    path("category/<path:path>/", products, name="products"),

    path("product/<str:slug>/", product, name="product"),

    path("", include(router.urls), name="products1"),
    path("variations/", VariationListAPIView.as_view(), name="variations"),
]
