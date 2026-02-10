from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderItem(models.Model):
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Заказ"),
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("Продукт"),
    )
    store = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("Магазин"),
    )
    price = models.PositiveIntegerField(
        verbose_name=_("Цена за единицу"),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Количество"),
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата обновления"),
    )

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"
    
    class Meta:
        verbose_name = _("Позиция заказа")
        verbose_name_plural = _("Позиции заказов")