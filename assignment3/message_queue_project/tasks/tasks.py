from celery import shared_task
from django.core.mail import send_mail
from celery.exceptions import Retry
import time

@shared_task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, body):
    try:
        send_mail(
            subject,
            body,
            'your_email@example.com', 
            [recipient]
        )
    except Exception as exc:
        time.sleep(5) 
        raise self.retry(exc=exc)
