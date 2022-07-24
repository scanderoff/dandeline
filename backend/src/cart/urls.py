from django.urls import path, URLPattern

from . import views

app_name: str = "cart"

urlpatterns: list[URLPattern] = [
    path("", views.summary, name="summary"),
    path("clear/", views.clear, name="clear"),
    path("update/", views.update, name="update"),
    path("remove/", views.remove, name="remove"),
]
