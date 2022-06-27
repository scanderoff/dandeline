from typing import Any, Sequence

from django import forms
from django.contrib.auth import get_user_model
# from django.utils.translation import gettext as _
from django.db.models import Model

from core.mixins import FormCleanMixin
from .models import Order


User: type[Model] = get_user_model()


class OrderCreateForm(forms.ModelForm, FormCleanMixin):
    class Meta:
        model: type[Model] = Order
        fields: Sequence[str] = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "zip_code",
            "city",
            "address1",
            "address2",
            "shipping_method",
            "payment_method",
            "note",
        ]

        widgets: dict[str, type[forms.Widget] | forms.Widget] = {
            "first_name": forms.TextInput(attrs={"class": "input__field"}),
            "last_name": forms.TextInput(attrs={"class": "input__field"}),
            "phone": forms.TextInput(attrs={"type": "tel", "class": "input__field", "data-phone-field": ""}),
            "email": forms.EmailInput(attrs={"class": "input__field"}),
            "zip_code": forms.TextInput(attrs={"class": "input__field"}),
            "city": forms.TextInput(attrs={"class": "input__field"}),
            "address1": forms.TextInput(attrs={"class": "input__field", "placeholder": "Название улицы и номер дома"}),
            "address2": forms.TextInput(attrs={"class": "input__field", "placeholder": "Квартира"}),
            "shipping_method": forms.RadioSelect,
            "payment_method": forms.RadioSelect,
            "note": forms.Textarea(attrs={
                "class": "input__field",
                "placeholder": ("Оставьте комментарий к заказу,"
                                "например особые пожелания отделу доставки"),
                "rows": 0,
                "cols": 0
            }),
        }

        labels: dict[str, str] = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "phone": "Телефон",
            "email": "E-mail",
            "zip_code": "Индекс",
            "city": "Город",
            "address1": "Адрес",
            "address2": "",
            "shipping_method": "",
            "payment_method": "",
            "note": "Примечание к заказу (необязательно)",
        }

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)

    @classmethod
    def from_user(cls, user: User):
        if not user.is_authenticated:
            return cls()

        return cls(initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "email": user.email,
            "zip_code": user.zip_code,
            "city": user.city,
            "address1": user.address1,
            "address2": user.address2,
        })
