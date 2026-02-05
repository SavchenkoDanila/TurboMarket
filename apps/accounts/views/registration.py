from django.views.generic import FormView
from django.urls import reverse_lazy

from apps.accounts.forms import RegistrationForm
from apps.accounts.services.registration import RegistrationService

class RegistrationView(FormView):
    template_name = "accounts/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("accounts:otp_confirm")

    def form_valid(self, form):
        RegistrationService.register(
            email=form.cleaned_data["email"],
            nickname=form.cleaned_data["nickname"],
            password=form.cleaned_data["password"],
        )

        self.request.session['pending_email'] = form.cleaned_data["email"]
        return super().form_valid(form)
    