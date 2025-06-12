import os
from celery import shared_task
from django.core.mail import send_mail

@shared_task(name="send_welcome_email")
def send_welcome_email(email: str) -> None:
    """
    Celery task to send a welcome email to the registered user.
    """
    subject = 'Welcome to UserConnect API!'
    message = 'Hi there,\n\nThanks for registering with us!'
    from_email = os.getenv("EMAIL_HOST_USER")

    if not from_email:
        print(" EMAIL_HOST_USER is not set in environment variables.")
        return

    send_mail(subject, message, from_email, [email])
