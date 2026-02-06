from django.shortcuts import render


def password_reset_success_view(request):
    return render(request, "accounts/password_reset/password_reset_success.html")