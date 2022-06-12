from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns: list[URLPattern] = [
    # path("", views.sign_in, name="login"),
    path("", auth_views.LoginView.as_view(), name="login"),
]
