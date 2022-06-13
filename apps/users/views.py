from typing import Any

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Model

from .forms import LoginForm, RegisterForm, EditForm


User: type[Model] = get_user_model()


@require_GET
def auth(request: HttpRequest) -> HttpResponse:
    login_form = LoginForm()
    register_form = RegisterForm()

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
            return HttpResponse("Invalid login data")

        if not user.is_active:
            return HttpResponse("Disabled account")

        login(request, user)

        next: str = request.POST["next"]

        return redirect(next if next else "users:edit")


    return render(request, "users/auth.html", {
        "login_form": form,
        "register_form": RegisterForm(),
    })


@require_POST
def user_register(request: HttpRequest) -> HttpResponse:
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
        new_password1: str = cd["new_password1"]
        new_password2: str = cd["new_password2"]

        if all((current_password, new_password1, new_password2)):
            user.change_password(current_password, new_password1, new_password2)
            print("PASSWORD CHANGED")

        user.save()
        print(form.cleaned_data)

    return render(request, "users/edit.html", {
        "section": "profile",
        "form": form,
    })
