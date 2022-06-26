from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Size


class FilterForm(forms.Form):
    MIN_PRICE = 0
    MAX_PRICE = 10_000

    size = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    price_from = forms.IntegerField(
        label="от",
        initial=MIN_PRICE,
        min_value=MIN_PRICE,
        max_value=MAX_PRICE,
        validators=[
            MinValueValidator(MIN_PRICE),
            MaxValueValidator(MAX_PRICE),
        ],
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "price-input__field price-input__field--from",
        }),
    )

    price_to = forms.IntegerField(
        label="до",
        initial=MAX_PRICE,
        min_value=MIN_PRICE,
        max_value=MAX_PRICE,
        validators=[
            MinValueValidator(MIN_PRICE),
            MaxValueValidator(MAX_PRICE),
        ],
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "price-input__field price-input__field--to",
        }),
    )
