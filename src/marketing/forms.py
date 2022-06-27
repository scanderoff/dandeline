from typing import Sequence

from django import forms
from django.db.models import Model

from core.mixins import FormCleanMixin
from .models import Contact


class ContactForm(forms.ModelForm, FormCleanMixin):
    class Meta:
        model: type[Model] = Contact
        fields: Sequence[str] = ("name", "phone")

        widgets: dict[str, type[forms.Widget] | forms.Widget] = {
            "name": forms.TextInput(attrs={
                "class": "input__field",
                "placeholder": "Имя",
            }),

            "phone": forms.TextInput(attrs={
                "class": "input__field",
                "type": "tel",
                "placeholder": "Телефон",
                "data-phone-field": "",
            }),
        }
