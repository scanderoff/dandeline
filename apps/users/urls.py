from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.auth, name="auth"),
    path("login/", views.user_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.user_register, name="register"),

    path("edit/", views.user_edit, name="edit"),
    path("orders/", views.user_orders, name="orders"),
    path("order/<int:order_id>", views.user_order, name="order"),
]
