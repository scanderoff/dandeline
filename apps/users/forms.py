from typing import Any, Sequence

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.db.models import Model


class FormCleanMixin:
    def clean_phone(self) -> str:
        phone: str = self.cleaned_data["phone"]
        unmasked: str = "".join(ch for ch in phone if ch.isdigit())

        return unmasked


class LoginForm(forms.Form, FormCleanMixin):
    phone = forms.CharField(
        label="Логин (номер телефона в формате +79999999999)",
        widget=forms.TextInput(attrs={
            "type": "tel",
            "class": "input__field",
            "data-phone-field": "",
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input__field"}),
    )

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)


class RegisterForm(forms.ModelForm, FormCleanMixin):
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
        widgets: dict[str, type[forms.Widget] | forms.Widget] = {
            "phone": forms.TextInput(attrs={
                "class": "input__field",
                "type": "tel",
                "data-phone-field": "",
            }),
        }

        labels: dict[str, str] = {
            "phone": "Телефон",
        }

        error_messages: dict[str, dict[str, str]] = {
            "phone": {
                "unique": "Пользователь с таким номером уже зарегистрирован",
            },
        }

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)

    def clean_password2(self) -> str:
        cd: dict[str, Any] = self.cleaned_data

        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают.")

        return cd["password2"]


class EditForm(forms.ModelForm, FormCleanMixin):
    current_password = forms.CharField(
        label="Сменить пароль",
        widget=forms.PasswordInput(attrs={
            "class": "input__field",
            "placeholder": "Введите текущий пароль",
        }),
        required=False,
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "class": "input__field",
            "placeholder": "Введите новый пароль",
        }),
        required=False,
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "class": "input__field",
            "placeholder": "Подтвердите новый пароль",
        }),
        required=False,
    )

    class Meta:
        model: type[Model] = get_user_model()

        fields: Sequence[str] = (
            "first_name",
            "last_name",
            "phone",
            "birthdate",
            "zip_code",
            "city",
            "address1",
            "address2",
            "gender",
        )

        widgets: dict[str, type[forms.Widget] | forms.Widget] = {
            "first_name": forms.TextInput(attrs={"class": "input__field"}),
            "last_name": forms.TextInput(attrs={"class": "input__field"}),
            "phone": forms.TextInput(attrs={
                "type": "tel",
                "class": "input__field",
                "data-phone-field": "",
            }),
            "birthdate": forms.TextInput(attrs={"class": "input__field"}),
            "zip_code": forms.TextInput(attrs={"class": "input__field"}),
            "city": forms.TextInput(attrs={"class": "input__field"}),
            "address1": forms.TextInput(
                attrs={
                    "class": "input__field",
                    "placeholder": "Название улицы и номер дома"
                }
            ),
            "address2": forms.TextInput(
                attrs={"class": "input__field", "placeholder": "Квартира"}
            ),
            "gender": forms.RadioSelect,
        }

        labels: dict[str, str] = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "phone": "Телефон",
            "birthdate": "Дата рождения",
            "zip_code": "Индекс",
            "city": "Город/населённый пункт",
            "address1": "Улица, дом",
            "address2": "",
            "gender": "Пол",
        }

    def clean(self) -> str:
        cd: dict[str, Any] = super().clean()
        current_password: str = cd.get("current_password")
        new_password1: str = cd.get("password1")
        new_password2: str = cd.get("password2")

        if not all((current_password, new_password1, new_password2)):
            return cd

        if not check_password(current_password, self.instance.password):
            self.add_error("current_password", "Неверный пароль.")

        if new_password1 != new_password2:
            self.add_error("password1", "Пароли должны совпадать.")
            self.add_error("password2", "Пароли должны совпадать.")

        return cd
