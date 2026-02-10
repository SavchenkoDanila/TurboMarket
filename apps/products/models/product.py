from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from apps.products.enums.product_statuses import ProductStatuses


class Product(models.Model):
    store = models.ForeignKey(
        "stores.Store", 
        on_delete=models.CASCADE, 
        related_name="products", 
        verbose_name=_("Магазин")
    )
    name = models.CharField(
        max_length=255, 
        verbose_name=_("Название продукта")
    )
    description = models.TextField(
        blank=True, 
        verbose_name=_("Описание продукта")
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        verbose_name=_("Slug продукта")
    )
    price = models.PositiveIntegerField(
        verbose_name=_("Цена продукта")
    )
    is_available = models.BooleanField(
        default=True, 
        verbose_name=_("Доступность продукта")
    )
    status = models.CharField(
        max_length=20, 
        choices=ProductStatuses.choices, 
        default=ProductStatuses.DRAFT, 
        verbose_name=_("Статус продукта")
    )
    category = models.ForeignKey(
        "products.ProductCategory", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="products", 
        verbose_name=_("Категория продукта")
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
        return f"{self.name} (Store: {self.store.name})"
    
    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={
            'store_slug': self.store.slug,
            'product_slug': self.slug
        })

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")
        ordering = ["-created_at", "name"]