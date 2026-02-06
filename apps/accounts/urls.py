from django.urls import path

from apps.accounts.views.registration import RegistrationView
from apps.accounts.views.authorization import UserLoginView
from apps.accounts.views.otp import OTPConfirmView


app_name = "accounts"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("otp-confirm/", OTPConfirmView.as_view(), name="otp_confirm"),
]
