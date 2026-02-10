import random
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth import get_user_model

from apps.accounts.models.authentication import AuthCode
from apps.accounts.tasks.send_otp import send_email_with_code_task


User = get_user_model()


class RegistrationService:
    @staticmethod
    def register(email, nickname, password):
        user = User.objects.create_user(
            email=email,
            username=nickname,
            password=password,
            is_active=False
        )

        code = str(random.randint(100000, 999999))

        AuthCode.objects.filter(user=user, is_used=False).update(is_used=True)
        AuthCode.objects.create(
            user=user, 
            code=code, 
            expires_at=timezone.now() + timedelta(minutes=15)
        )

        send_email_with_code_task.delay(email, code) 
        return user