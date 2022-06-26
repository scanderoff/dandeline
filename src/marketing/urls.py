from django.urls import URLPattern, path

from .apps import MarketingConfig
from . import views


app_name: str = MarketingConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.homepage, name="homepage"),
]
