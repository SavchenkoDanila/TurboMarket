from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatuses(models.TextChoices):
    PENDING = "pending", _("Ожидает оплаты")
    CANCELED = "canceled", _("Отменен")
    COMPLETED = "completed", _("Завершен")
    REFUNDED = "refunded", _("Возвращен")

    