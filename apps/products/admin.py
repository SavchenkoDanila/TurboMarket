from django.contrib import admin

from apps.products.models import (
    Product,
    ProductCategory,
    ProductTextContent,
    ProductStats,
)


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTextContent)
admin.site.register(ProductStats)
