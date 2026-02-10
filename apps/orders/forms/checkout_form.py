from django import forms
from django.utils.translation import gettext_lazy as _


class CheckoutForm(forms.Form):
    email = forms.EmailField(
        label=_("Email для отправки заказа"),
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": _("Введите ваш email")}),
    )
    quantity = forms.IntegerField(
        label=_("Количество"),
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": _("Введите количество")}),
    )
    