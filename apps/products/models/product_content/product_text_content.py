from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductTextContent(models.Model):
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="text_content",
        verbose_name=_("Продукт"),
    )
    text_content = models.TextField(
        blank=True, 
        verbose_name=_("Текстовое содержание продукта")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата обновления")
    )

    def __str__(self):
        return f"TextContent for {self.product.name}"

    class Meta:
        verbose_name = _("Текстовое содержание продукта")
        verbose_name_plural = _("Текстовое содержание продуктов")