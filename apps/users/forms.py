from typing import Any

from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField(
        label="Логин (номер телефона в формате +79999999999)",
        widget=forms.TextInput(attrs={"type": "tel", "class": "input__field"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "input__field"})
    )

    def __init__(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, auto_id=False, **kwargs)
