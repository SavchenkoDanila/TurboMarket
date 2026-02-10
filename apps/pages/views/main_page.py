from django.views.generic import ListView

from apps.products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "pages/main.html"
    context_object_name = "products"
