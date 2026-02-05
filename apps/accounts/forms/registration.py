from django import forms
from django.utils.translation import gettext_lazy as _


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label=_("Адрес электронной почты"),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": _("Введите ваш email")}),
    )
    nickname = forms.CharField(
        label=_("Никнейм"),
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": _("Введите ваш никнейм")}),
    )
    password = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": _("Введите ваш пароль")}),
    )
    confirm_password = forms.CharField(
        label=_("Подтвердите пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": _("Подтвердите ваш пароль")}),
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError(_("Пароли не совпадают."))
        return cleaned_data
