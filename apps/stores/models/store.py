import uuid
import os

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Store(models.Model):
    def logo_upload_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{self.id}_{uuid.uuid4()}.{ext}"
        return os.path.join("stores/logos/", filename)
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="stores",
        verbose_name=_("Владелец магазина"),
    )
    name = models.CharField(
        max_length=255, 
        unique=True, 
        verbose_name=_("Название магазина"),
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        verbose_name=_("Слаг магазина"),
    )
    description = models.TextField(
        blank=True, 
        verbose_name=_("Описание магазина"),
    )
    logo = models.ImageField(
        upload_to=logo_upload_path,
        blank=True,
        null=True,
        verbose_name=_("Логотип магазина"),
        default="stores/logos/default_logo.png",
        help_text="Рекомендуемый формат: PNG/JPG. Размер до 1 МБ. Пропорции 1:1 или 4:3."
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
        return f"Store: {self.name} (Owner: {self.owner.username})"

    def get_absolute_url(self):
        return reverse('stores:store-detail', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = _("Магазин")
        verbose_name_plural = _("Магазины")
