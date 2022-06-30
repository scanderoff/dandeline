from typing import Any

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    get_user_model,
    update_session_auth_hash,
    login,
    authenticate,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet, Model

from orders.models import Order, OrderItem
from .forms import LoginForm, RegisterForm, EditForm


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

    form = LoginForm(request.POST)

    if form.is_valid():
        cd: dict[str, Any] = form.cleaned_data

        user: User = authenticate(request, username=cd["phone"],
                                  password=cd["password"])

        if user is None:
            return HttpResponse("User doesn't exist")

        if not user.is_active:
            return HttpResponse("User is disabled")

        login(request, user)

        if not cd["remember_me"]:
            request.session.set_expiry(0)

        next: str = request.POST["next"]

        return redirect(next if next else "users:edit")

    return render(request, "users/auth.html", {
        "login_form": form,
        "register_form": RegisterForm(),
    })


@require_POST
def signup(request: HttpRequest) -> HttpResponse:
    """Registration processing"""

    form = RegisterForm(request.POST)

    if form.is_valid():
        new_user: User = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password1"])
        new_user.save()

        login(request, new_user)

        next: str = request.POST["next"]

        return redirect(next if next else "users:edit")

    return render(request, "users/auth.html", {
        "login_form": LoginForm(),
        "register_form": form,
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


@login_required
def orders(request: HttpRequest) -> HttpResponse:
    """User order list"""

    orders: QuerySet[Order] = request.user.orders.all()

    # if not orders:
    #     messages.error(request, "У вас пока нет заказов")

    return render(request, "users/orders.html", {
        "section": "orders",
        "orders": orders,
    })


@login_required
def order(request: HttpRequest, order_id: int) -> HttpResponse:
    """User order"""

    order: Order = Order.objects.get(id=order_id)
    items: QuerySet[OrderItem] = order.items.select_related("variation").all()
    # TOFIX: дублируется запрос на подсчет конечной суммы
    print(items)
    return render(request, "users/order.html", {
        "section": "orders",
        "order": order,
        "items": items,
    })
