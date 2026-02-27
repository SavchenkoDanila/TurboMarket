from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        label=_("Адрес электронной почты"),
        max_length=254,
        widget=forms.EmailInput(attrs={"placeholder": _("Введите ваш email")}),
    )
    captcha = CaptchaField(
        label=_("Подтверждение"), 
        error_messages={'invalid': _("Неверный код капчи. Попробуйте снова.")},
    )
