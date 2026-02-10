from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from apps.orders.enums.order_statuses import OrderStatuses

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("Пользователь"),
    )
    email = models.EmailField(
        verbose_name=_("Email для отправки заказа"),
    )
    status = models.CharField(
        max_length=20,
        choices=OrderStatuses.choices,
        default=OrderStatuses.PENDING,
        verbose_name=_("Статус заказа"),
    )
    total_amount = models.PositiveIntegerField(
        verbose_name=_("Общая сумма заказа"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания заказа"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата обновления заказа"),
    )

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - Status: {self.status}"

    
    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
