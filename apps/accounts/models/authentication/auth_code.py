from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthCode(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="auth_codes",
        verbose_name=_("Пользователь"),
    )
    code = models.CharField(max_length=6, verbose_name=_("Код аутентификации"))
    expires_at = models.DateTimeField(verbose_name=_("Срок действия истекает"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    is_used = models.BooleanField(default=False, verbose_name=_("Статус использования"))

    def __str__(self):
        return f"AuthCode for {self.user.username} - {self.code} | Used: {self.is_used}"
