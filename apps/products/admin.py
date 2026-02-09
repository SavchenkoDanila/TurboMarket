from django.contrib import admin

from apps.products.models import *


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTextContent)
admin.site.register(ProductStats)
