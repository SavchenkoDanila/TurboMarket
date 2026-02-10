from django.views.generic import FormView
from django.shortcuts import get_object_or_404, redirect

from apps.orders.forms.checkout_form import CheckoutForm
from apps.orders.services.order_service import OrderService
from apps.orders.enums.order_statuses import OrderStatuses
from apps.orders.tasks.send_order_mail import send_email_with_order_task
from apps.products.models import Product

class CheckoutView(FormView):
    template_name = "orders/checkout.html"
    form_class = CheckoutForm

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, slug=kwargs['product_slug'], store__slug=kwargs['store_slug'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        quantity = form.cleaned_data['quantity']
        email = form.cleaned_data['email']

        order = OrderService.create_order(
            user = self.request.user,
            email=email,
            items=[{
                "product": self.product,
                "store": self.product.store,
                "price": self.product.price,
                "quantity": quantity,
            }],
        )
        order.status = OrderStatuses.COMPLETED
        order.save(update_fields=["status"])
        
        send_email_with_order_task.delay(email, order.id)
        return redirect("orders:success", order_id=order.id)