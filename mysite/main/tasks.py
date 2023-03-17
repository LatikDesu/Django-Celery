from celery import shared_task
from django.core.mail import send_mail
from .service import send


@shared_task()
def send_spam_email(user_email):
    send(user_email)


@shared_task()
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Ждите много спама.',
            'admin@gmail.com',
            [contact.email],
            fail_silently=False,
        )

