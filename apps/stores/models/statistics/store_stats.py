from django.db import models
from django.utils.translation import gettext_lazy as _


class StoreStats(models.Model):
    store = models.OneToOneField(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="statistics",
        verbose_name=_("Магазин"),
    )
    total_sales = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Всего продаж"),
    )
    rating = models.FloatField(
        default=0.0,
        verbose_name=_("Рейтинг"),
    )
    reviews_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Количество отзывов"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Создано"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Обновлено"),
    )
    recalculated_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Последний пересчёт"),
    )

    def __str__(self):
        return f"Statistics for Store ID:  {self.store.id}" 
    

    class Meta:
        verbose_name = _("Статистика магазина")
        verbose_name_plural = _("Статистика магазинов")