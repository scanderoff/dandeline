from typing import Any

from django import forms
from django.conf import settings
from django.forms import Widget
# from django.utils.translation import gettext as _
from django.db.models import Model

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model: type[Model] = Order
        exclude: list[str] = [
            "coupon",
            "discount",
            "user",
            "paid",
            "paid_at",
            "created_at",
        ]

        widgets: dict[str, type | Widget] = {
            "first_name": forms.TextInput(attrs={"class": "input__field"}),
            "last_name": forms.TextInput(attrs={"class": "input__field"}),
            "phone": forms.TextInput(attrs={"type": "tel", "class": "input__field"}),
            "email": forms.EmailInput(attrs={"class": "input__field"}),
            "zip_code": forms.TextInput(attrs={"class": "input__field"}),
            "city": forms.TextInput(attrs={"class": "input__field"}),
            "address_1": forms.TextInput(attrs={"class": "input__field", "placeholder": "Название улицы и номер дома"}),
            "address_2": forms.TextInput(attrs={"class": "input__field", "placeholder": "Квартира"}),
            "shipping_method": forms.RadioSelect,
            "payment_method": forms.RadioSelect,
            "note": forms.Textarea(attrs={"class": "input__field", "placeholder": "Оставьте комментарий к заказу, например особые пожелания отделу доставки", "rows": 0, "cols": 0}),
        }

        labels: dict[str, str] = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "phone": "Телефон",
            "email": "E-mail",
            "zip_code": "Индекс",
            "city": "Город",
            "address_1": "Адрес",
            "address_2": "",
            "shipping_method": "",
            "payment_method": "",
            "note": "Примечание к заказу (необязательно)",
        }

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)
