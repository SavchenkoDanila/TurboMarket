from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _

from apps.accounts.forms.authorization import AuthorizationForm
from apps.accounts.services.auth import AuthService


class AuthorizationView(FormView):
    template_name = "accounts/authorization.html"
    form_class = AuthorizationForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        user = AuthService.authenticate_user(request=self.request, email=email, password=password)
        
        if not user:
            form.add_error(None, _("Неверный email или пароль."))
            return self.form_invalid(form)
        
        if not user.is_active:
            form.add_error(None, _("Ваш аккаунт не активирован. Пожалуйста, подтвердите вашу электронную почту."))
            return self.form_invalid(form)
        
        login(self.request, user)
        return super().form_valid(form)