from django.urls import path, URLPattern

from .apps import BookmarkConfig
from . import views

app_name: str = BookmarkConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.summary, name="summary"),
    path("clear/", views.clear, name="clear"),
    path("update/<int:product_id>", views.update, name="update"),
]
