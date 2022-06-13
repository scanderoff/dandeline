from typing import Any, Sequence

from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Model


class LoginForm(forms.Form):
    phone = forms.CharField(
        label="Логин (номер телефона в формате +79999999999)",
        widget=forms.TextInput(attrs={
            "type": "tel",
            "class": "input__field",
            "autofocus": True,
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input__field"}),
    )

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input__field"})
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={"class": "input__field"})
    )

    class Meta:
        model: type[Model] = get_user_model()
        fields: Sequence[str] = ("phone",)
        widgets: dict[str, type | forms.Widget] = {
            "phone": forms.TextInput(attrs={"class": "input__field", "type": "tel"}),
        }
        labels: dict[str, str] = {
            "phone": "Телефон",
        }

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)

    def clean_password2(self) -> str:
        cd: dict[str, Any] = self.cleaned_data

        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают.")

        return cd["password2"]
