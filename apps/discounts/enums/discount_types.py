from django.db import models
from django.utils.translation import gettext_lazy as _


class DiscountTypes(models.TextChoices):
    PERCENTAGE = "percentage", _("Процентная скидка")
    FIXED_AMOUNT = "fixed_amount", _("Фиксированная сумма")