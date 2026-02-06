from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


user = get_user_model()


class PasswordResetNewPasswordForm(forms.Form):
    password = forms.CharField(
        label=_("Новый пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": _("Введите новый пароль")}),
    )
    confirm_password = forms.CharField(
        label=_("Подтвердите новый пароль"),
        widget=forms.PasswordInput(attrs={"placeholder": _("Подтвердите новый пароль")}),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError(_("Пароли не совпадают."))
        
        if self.user and self.user.check_password(cleaned_data.get("password")):
            raise forms.ValidationError(_("Новый пароль не должен совпадать с текущим паролем."))
        return cleaned_data