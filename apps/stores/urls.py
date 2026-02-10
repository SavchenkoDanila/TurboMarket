from django.urls import path

from apps.stores.views.store_detail import StoreDetailView

app_name = 'stores'

urlpatterns = [
    path('<slug:store_slug>/', StoreDetailView.as_view(), name='store-detail'),
]