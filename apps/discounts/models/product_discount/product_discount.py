from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.discounts.enums import DiscountTypes


class ProductDiscount(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="discounts",
        verbose_name=_("Продукт"),
    )
    discount_type = models.CharField(
        choices=DiscountTypes.choices, 
        max_length=20, 
        verbose_name=_("Тип скидки")
    )
    value = models.PositiveIntegerField(verbose_name=_("Значение скидки"))
    is_active = models.BooleanField(default=False, verbose_name=_("Активна"))
    start_date = models.DateTimeField(verbose_name=_("Дата начала"))
    end_date = models.DateTimeField(verbose_name=_("Дата окончания"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return f"{self.product.name} - {self.value} {self.get_discount_type_display()} (from {self.start_date} to {self.end_date})"

    class Meta:
        verbose_name = _("Скидка на продукт")
        verbose_name_plural = _("Скидки на продукты")