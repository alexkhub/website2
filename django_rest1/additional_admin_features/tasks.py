from django_rest1.celery import app
from shop.models import Users
from .service import *
from django.core.mail import send_mail
@app.task
def send_emails(mail_text):
    users = Users.objects.filter(mailing_list=True)
    for user in users:
        send_mail(
            'Акции',
            mail_text,
            'aleksandrkhubaevwork@gmail.com',
            [user.email],
            fail_silently=False

        )
    return None
@app.task
def send_spam():
        send_mail(
            'Акции',
            'хай бебра',
            'aleksandrkhubaevwork@gmail.com',
            ['aleksandrkhubaev04@gmail.com'],
            fail_silently=False
            )

