from django import forms
from django.utils.translation import gettext_lazy as _


class PasswordResetConfirm(forms.Form):
    code = forms.CharField(
        label=_("Код подтверждения"),
        max_length=6,
        widget=forms.TextInput(attrs={"placeholder": _("Введите код подтверждения")}),
    )