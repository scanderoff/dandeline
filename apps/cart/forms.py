from django import forms


class CartUpdateForm(forms.Form):
    quantity = forms.CharField(widget=forms.TextInput(attrs={"class": "qty-input__field"}))