from django.db import models
from django.utils.translation import gettext_lazy as _


class BuyerProfile(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="buyer_profile",
        verbose_name=_("Пользователь"),
    )
    discount_level = models.PositiveIntegerField(
        default=0, verbose_name=_("Уровень скидки")
    )

    def __str__(self):
        return f"BuyerProfile of {self.user.username}"
