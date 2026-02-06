from django import forms
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField


class AuthorizationForm(forms.Form):
    email = forms.EmailField(
        label=_("Адрес электронной почты"),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": _("Введите ваш email")}),
    )
    password = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": _("Введите ваш пароль")}),
    )
    captcha = CaptchaField(
        label=_("Подтверждение"), 
        error_messages={'invalid': _("Неверный код капчи. Попробуйте снова.")},
    )