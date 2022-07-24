from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.auth, name="auth"),
    path("login/", views.signin, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.signup, name="register"),

    path("edit/", views.user_edit, name="edit"),
    path("orders/", views.orders, name="orders"),
    path("order/<int:order_id>/", views.order, name="order"),
]
