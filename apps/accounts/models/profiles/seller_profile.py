from django.db import models
from django.utils.translation import gettext_lazy as _


class SellerProfile(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="seller_profile",
        verbose_name=_("Пользователь"),
    )
    verification_status = models.BooleanField(
        default=False, verbose_name=_("Статус верификации")
    )
    rating = models.FloatField(default=0.0, verbose_name=_("Рейтинг продавца"))

    def __str__(self):
        return f"SellerProfile of {self.user.username}"


    class Meta:
        verbose_name = _("Профиль продавца")
        verbose_name_plural = _("Профили продавцов")