from django.contrib import admin

from apps.stores.models import Store
from apps.stores.models.statistics import StoreStats

admin.site.register(Store)
admin.site.register(StoreStats)
