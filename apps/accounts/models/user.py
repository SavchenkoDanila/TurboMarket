from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.enums import Roles


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_("Электронная почта"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Статус активности"))
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.BUYER,
        verbose_name=_("Роль пользователя"),
    )
    last_login = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Последний вход")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} ({self.email}) | Role: {self.role} | Active: {self.is_active}"


    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")