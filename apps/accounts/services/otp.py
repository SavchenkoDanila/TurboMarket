from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.authentication import AuthCode

User = get_user_model()

class OTPService:
    @staticmethod
    def confirm(email, code):
        user = get_object_or_404(User, email=email)

        auth_code = (
            AuthCode.objects.filter(user=user, is_used=False)
            .order_by("-created_at")
            .first()
        )

        if not auth_code:
            raise ValueError(_("Код подтверждения не найден.")) 
        if auth_code.expires_at < timezone.now():
            raise ValueError(_("Код подтверждения истек."))
        if auth_code.code != code:
            raise ValueError(_("Неверный код подтверждения."))
        
        auth_code.is_used = True
        auth_code.save()

        user.is_active = True
        user.save()

        return user