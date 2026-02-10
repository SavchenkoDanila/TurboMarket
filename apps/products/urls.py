from django.urls import path

from apps.products.views.product_detail import ProductDetailView

app_name = 'products'

urlpatterns = [
    path('<slug:store_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product-detail'),
]