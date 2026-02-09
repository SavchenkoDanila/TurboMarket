from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductStatuses(models.TextChoices):
    DRAFT = "draft", _("Черновик")
    ACTIVE = "active", _("Активный")
    INACTIVE = "inactive", _("Неактивный")
    BLOCKED = "blocked", _("Заблокированный")