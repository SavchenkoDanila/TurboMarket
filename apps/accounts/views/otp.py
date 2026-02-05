from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from apps.accounts.forms import OTPConfirmForm
from apps.accounts.services.otp import OTPService


class OTPConfirmView(FormView):
    template_name = "accounts/otp_confirm.html"
    form_class = OTPConfirmForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        email = self.request.session.get('pending_email')
        
        if not email:
            messages.error(self.request, _("Сессия истекла. Пожалуйста, начните регистрацию заново."))
            return self.form_invalid(form)
        
        try:
            OTPService.confirm(email=email, code=form.cleaned_data["code"])
        except ValueError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)
        
        messages.success(self.request, _("Ваш аккаунт успешно подтвержден."))
        del self.request.session['pending_email']

        return super().form_valid(form)