from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name=_("Название категории")
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        verbose_name=_("Slug категории")
    )
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="subcategories",
        null=True,
        blank=True,
        verbose_name=_("Родительская категория")
    )
    sort_order = models.PositiveIntegerField(
        default=0, 
        verbose_name=_("Порядок сортировки")
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
        return f"{self.name} (Parent: {self.parent_category.name if self.parent_category else 'No parent'})"

    class Meta:
        verbose_name = _("Категория продукта")
        verbose_name_plural = _("Категории продуктов")
        ordering = ["sort_order", "name"]
