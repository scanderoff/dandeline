from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import views
from .forms import LoginForm


def sign_in(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form: LoginForm = LoginForm()
    else:
        form: LoginForm = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(request, username=cd["phone"], password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")

    return render(request, "users/auth.html", {
        "login_form": form,
    })
