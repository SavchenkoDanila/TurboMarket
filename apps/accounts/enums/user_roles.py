from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    BUYER = "buyer", _("Покупатель")
    SELLER = "seller", _("Продавец")
    ADMIN = "admin", _("Администратор")
    MODERATOR = "moderator", _("Модератор")
