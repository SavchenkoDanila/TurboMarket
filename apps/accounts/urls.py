from django.urls import path

from apps.accounts.views import RegistrationView, UserLoginView, OTPConfirmView

app_name = "accounts"

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("otp-confirm/", OTPConfirmView.as_view(), name="otp_confirm"),
]
