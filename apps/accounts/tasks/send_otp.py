from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_with_code_task(email, code):
    subject = "Ваш код подтверждения"
    message = f"Ваш код подтверждения: {code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)