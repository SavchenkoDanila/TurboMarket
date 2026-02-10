from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_with_order_task(email, order_id):
    subject = "Ваш заказ успешно оформлен"
    message = f"Благодарим за покупку! Ваш заказ успешно оформлен. Номер заказа: {order_id}. Ожидайте письмо с подтверждением на ваш email."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
