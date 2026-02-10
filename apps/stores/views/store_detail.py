from django.views.generic import DetailView

from apps.stores.models import Store


class StoreDetailView(DetailView):
    model = Store
    template_name = "stores/store_detail.html"
    context_object_name = "store"
    slug_field = "slug"
    slug_url_kwarg = "store_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.products.all()
        return context