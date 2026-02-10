from django.db import transaction

from apps.orders.models import Order, OrderItem
from apps.orders.enums.order_statuses import OrderStatuses


class OrderService:
    @staticmethod
    @transaction.atomic
    def create_order(user, email, items):
        order = Order.objects.create(
            user=user,
            email=email,
            status=OrderStatuses.PENDING,
            total_amount=0,
        )

        total = 0

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                store=item["store"],
                price=item["price"],
                quantity=item["quantity"],
            )
            total += item["price"] * item["quantity"]

        order.total_amount = total
        order.save(update_fields=["total_amount"])

        return order
