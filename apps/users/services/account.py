from typing import Any

from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.http import HttpRequest
from django.db.models import QuerySet, Model
from django.forms import ValidationError

from orders.models import Order, OrderItem
from ..forms import EditForm


User: type[Model] = get_user_model()


class Account:
    """Account manager"""

    def __init__(self) -> None:
        self.edit_form = None

    def update(self, request: HttpRequest) -> None:
        self.edit_form = EditForm(instance=request.user, data=request.POST)

        if not self.edit_form.is_valid():
            raise ValidationError()

        user: User = self.edit_form.save(commit=False)

        cd: dict[str, Any] = self.edit_form.cleaned_data

        current_password: str = cd["current_password"]
        new_password1: str = cd["password1"]
        new_password2: str = cd["password2"]

        if all((current_password, new_password1, new_password2)):
            user.set_password(new_password1)
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль успешно изменен")

        user.save()

    def get_orders(self) -> QuerySet[Order]:
        orders: QuerySet[Order] = self.request.user.orders.all()

        return orders
