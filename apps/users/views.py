from typing import Any

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Model

from .forms import LoginForm, RegistrationForm


User: type[Model] = get_user_model()


@require_GET
def auth(request: HttpRequest) -> HttpResponse:
    login_form: LoginForm = LoginForm()
    register_form: RegistrationForm = RegistrationForm()

    return render(request, "users/auth.html", {
        "login_form": login_form,
        "register_form": register_form,
    })


@require_POST
def user_login(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST)

    if form.is_valid():
        cd: dict[str, Any] = form.cleaned_data

        user: User = authenticate(request, username=cd["phone"],
                                  password=cd["password"])

        if user is None:
            return HttpResponse("Invalid login")

        if not user.is_active:
            return HttpResponse("Disabled account")

        login(request, user)

        return HttpResponse("Authenticated successfully")


    return render(request, "users/auth.html", {
        "login_form": form,
    })


@require_POST
def user_register(request: HttpRequest) -> HttpResponse:
    form = RegistrationForm(request.POST)

    if form.is_valid():
        new_user: User = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password1"])
        new_user.save()

    return render(request, "users/register_done.html", {
        "new_user": new_user,
    })
