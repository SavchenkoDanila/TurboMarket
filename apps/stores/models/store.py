from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Store(models.Model):
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
        upload_to="stores/logos/",
        blank=True,
        null=True,
        verbose_name=_("Логотип магазина"),
        default="stores/logos/default_logo.png",
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