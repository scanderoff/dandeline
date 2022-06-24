from typing import Any

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet, Model
from django.forms import ValidationError

from orders.models import Order, OrderItem
from .forms import LoginForm, RegisterForm, EditForm
from .services.authentication import SignUpProcessor, SignInProcessor
from .services.account import Account
from .services.exceptions import DisabledUserError


User: type[Model] = get_user_model()


@require_GET
def auth(request: HttpRequest) -> HttpResponse:
    """Render login and registration forms"""
    if request.user.is_authenticated:
        return redirect("users:edit")

    login_form = LoginForm()
    register_form = RegisterForm()

    return render(request, "users/auth.html", {
        "login_form": login_form,
        "register_form": register_form,
    })


@require_POST
def signin(request: HttpRequest) -> HttpResponse:
    """Login processing"""
    signin_processor = SignInProcessor(request)

    try:
        signin_processor.signin()
    except User.DoesNotExist:
        ...
    except DisabledUserError:
        messages.error("Данный аккаунт отключен")
    except ValidationError:
        messages.error("Проверьте правильность заполнения формы")
    else:
        next: str = request.POST["next"]

        return redirect(next if next else "users:edit")

    return render(request, "users/auth.html", {
        "login_form": signin_processor.signin_form,
        "register_form": RegisterForm(),
    })


@require_POST
def signup(request: HttpRequest) -> HttpResponse:
    """Registration processing"""
    signup_processor = SignUpProcessor(request)

    try:
        signup_processor.signup()

        next: str = request.POST["next"]

        return redirect(next if next else "users:edit")
    except ValidationError:
        messages.error("Проверьте правильность заполнения формы")

    return render(request, "users/auth.html", {
        "login_form": LoginForm(),
        "register_form": signup_processor.form,
    })


@login_required
def user_edit(request: HttpRequest) -> HttpRequest:
    if request.method == "GET":
        form = EditForm(instance=request.user)
    else:
        form = EditForm(instance=request.user, data=request.POST)

        if form.is_valid():
            user: User = form.save(commit=False)

            cd: dict[str, Any] = form.cleaned_data
            current_password: str = cd["current_password"]
            new_password1: str = cd["password1"]
            new_password2: str = cd["password2"]

            if all((current_password, new_password1, new_password2)):
                user.set_password(new_password1)
                update_session_auth_hash(request, user)
                messages.success(request, "Пароль успешно изменен")

            user.save()
        else:
            messages.success(request, "Проверьте правильность заполнения полей")

    return render(request, "users/edit.html", {
        "section": "profile",
        "form": form,
    })


# @login_required
# def edit(request: HttpRequest) -> HttpResponse:
#     account = Account(request)



#     return render(request, "users/edit.html", {
#         "section": "profile",
#         "form": account.edit_form,
#     })


@login_required
def orders(request: HttpRequest) -> HttpResponse:
    orders: QuerySet[Order] = request.user.orders.all()

    return render(request, "users/orders.html", {
        "section": "orders",
        "orders": orders,
    })


@login_required
def order(request: HttpRequest, order_id: int) -> HttpResponse:
    order: Order = Order.objects.get(id=order_id)
    items: QuerySet[OrderItem] = order.items.select_related("variation").all()
    # TOFIX: дублируется запрос на подсчет конечной суммы

    return render(request, "users/order.html", {
        "section": "orders",
        "order": order,
        "items": items,
    })
