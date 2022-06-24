from typing import Any

from django.db.models import Model
from django.contrib.auth import get_user_model, authenticate, login
from django.forms import ValidationError
from django.http import HttpRequest

from .exceptions import DisabledUserError
from ..forms import RegisterForm, LoginForm


User: type[Model] = get_user_model()


class SignUpProcessor:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.form = RegisterForm(self.request.POST)

    def signup(self, auto_signin: bool = True) -> User:
        if not self.form.is_valid():
            raise ValidationError()

        new_user: User = self.form.save(commit=False)
        new_user.set_password(self.form.cleaned_data["password1"])
        new_user.save()

        if auto_signin:
            login(self.request, new_user)

        return new_user


class SignInProcessor:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.form = LoginForm(self.request.POST)

    def signin(self) -> None:
        if not self.form.is_valid():
            raise ValidationError()

        cd: dict[str, Any] = self.form.cleaned_data

        user: User = authenticate(self.request, username=cd["phone"],
                                  password=cd["password"])

        if user is None:
            raise User.DoesNotExist()

        if not user.is_active:
            raise DisabledUserError()

        login(self.request, user)
