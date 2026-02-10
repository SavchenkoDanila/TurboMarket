from django.urls import path

from apps.orders.views.checkout import CheckoutView
from apps.orders.views.success import OrderSuccessView


app_name = "orders"

urlpatterns = [
    path('checkout/<slug:store_slug>/<slug:product_slug>/', CheckoutView.as_view(), name='checkout'),
    path('success/<int:order_id>/', OrderSuccessView.as_view(), name='success'),
]