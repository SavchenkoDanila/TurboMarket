from django import forms
from django.utils.translation import gettext_lazy as _


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        label=_("Адрес электронной почты"),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": _("Введите ваш email")}),
    )

