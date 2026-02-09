from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductStats(models.Model):
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="stats",
        verbose_name=_("Продукт"),
    )
    views_count = models.PositiveIntegerField(
        default=0, 
        verbose_name=_("Количество просмотров")
    )
    purchases_count = models.PositiveIntegerField(
        default=0, 
        verbose_name=_("Количество покупок")
    )
    favorites_count = models.PositiveIntegerField(
        default=0, 
        verbose_name=_("Количество добавлений в избранное")
    )
    reviews_count = models.PositiveIntegerField(
        default=0, 
        verbose_name=_("Количество отзывов")
    )
    rating = models.FloatField(
        default=0.0, 
        verbose_name=_("Рейтинг продукта")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Дата обновления")
    )
    recalculated_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Дата последнего пересчета статистики")
    )

    def __str__(self):
        return f"Stats for {self.product.name}"

    class Meta:
        verbose_name = _("Статистика продукта")
        verbose_name_plural = _("Статистика продуктов")