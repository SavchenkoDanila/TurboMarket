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
        required_fields = ["product", "store", "price", "quantity"]

        for item in items:
            if not all(item.get(field) for field in required_fields):
                raise ValueError(f"Некорректный item: отсутствуют обязательные поля — {item}")
            
            OrderItem.objects.create(
                order=order,
                product=item.get("product"),
                store=item.get("store"),
                price=item.get("price"),
                quantity=item.get("quantity"),
            )
            total += item.get("price") * item.get("quantity")

        order.total_amount = total
        order.save(update_fields=["total_amount"])

        return order
