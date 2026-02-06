from django.urls import path

from apps.accounts.views.registration import RegistrationView
from apps.accounts.views.authorization import AuthorizationView
from apps.accounts.views.otp import OTPConfirmView
from apps.accounts.views.password_reset.password_reset_confirm import PasswordResetConfirmView
from apps.accounts.views.password_reset.password_reset_new_password import PasswordResetNewPasswordView
from apps.accounts.views.password_reset.password_reset_request import PasswordResetRequestView
from apps.accounts.views.password_reset.password_reset_success import password_reset_success_view

app_name = "accounts"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="registration"),
    path("login/", AuthorizationView.as_view(), name="login"),
    path("otp-confirm/", OTPConfirmView.as_view(), name="otp_confirm"),
    path("password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path("password-reset/confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path("password-reset/new-password/", PasswordResetNewPasswordView.as_view(), name="password-reset-new-password"),
    path("password-reset/success/", password_reset_success_view, name="password-reset-success"),
]
