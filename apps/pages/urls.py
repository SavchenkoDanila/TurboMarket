from django.urls import path

from apps.pages.views.main_page import ProductListView

app_name = 'pages'

urlpatterns = [
    path('', ProductListView.as_view(), name='main-page'),
]