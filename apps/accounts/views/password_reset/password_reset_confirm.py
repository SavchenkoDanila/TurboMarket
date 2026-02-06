from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from apps.accounts.forms.password_reset.password_reset_confirm import (
    PasswordResetConfirm,
)
from apps.accounts.services.otp import OTPService


class PasswordResetConfirmView(FormView):
    template_name = "accounts/password_reset/password_reset_confirm.html"
    form_class = PasswordResetConfirm
    success_url = reverse_lazy("accounts:password-reset-new-password")

    def form_valid(self, form):
        email = self.request.session.get('reset_email')

        if not email:
            messages.error(self.request, _("Сессия истекла. Пожалуйста, начните процесс сброса пароля заново."))
            return self.form_invalid(form)
        
        try:
            OTPService.confirm(email=email, code=form.cleaned_data["code"])
        except ValueError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)
        
        self.request.session['reset_confirmed'] = True
        return super().form_valid(form)