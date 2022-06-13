from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.auth, name="auth"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
]
