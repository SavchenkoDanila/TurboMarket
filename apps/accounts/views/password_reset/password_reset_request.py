from django.views.generic import FormView
from django.urls import reverse_lazy

from apps.accounts.forms.password_reset.password_reset_request import (
    PasswordResetRequestForm,
)
from apps.accounts.services.password_reset import PasswordResetService


class PasswordResetRequestView(FormView):
    template_name = "accounts/password_reset/password_reset_request.html"
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy("accounts:password-reset-confirm")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        PasswordResetService.send_reset_code(email=email)
        self.request.session['reset_email'] = email
        return super().form_valid(form)