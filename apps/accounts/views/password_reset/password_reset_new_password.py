from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from apps.accounts.forms.password_reset.password_reset_new_password import (
    PasswordResetNewPasswordForm,
)


User = get_user_model()


class PasswordResetNewPasswordView(FormView):
    template_name = "accounts/password_reset/password_reset_new_password.html"
    form_class = PasswordResetNewPasswordForm
    success_url = reverse_lazy("accounts:password-reset-success")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        email = self.request.session.get('reset_email')
        if email:
            kwargs['user'] = User.objects.get(email=email)
        return kwargs

    def form_valid(self, form):
        if not self.request.session.get('reset_confirmed'):
            messages.error(self.request, _("Сначала подтвердите сброс пароля."))
            return self.form_invalid(form)
        
        email = self.request.session.get('reset_email')
        user = User.objects.get(email=email)

        user.set_password(form.cleaned_data["password"])
        user.save()

        del self.request.session['reset_email']
        del self.request.session['reset_confirmed']

        return super().form_valid(form)