from django_rest1.celery import app
from shop.models import Users, Transactions
from .service import *
from django.core.mail import send_mail
from .models import *

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


@app.task(bind=True, default_retry_delay=5 * 60)  # таска будет перезапускаться каждые 5 минут
def plus(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task
def sales_analysis():
    day = yesterday()
    transactions = Transactions.objects.filter(transaction_date__contains =day)
    sum = 0
    for transaction in transactions:
        sum += transaction.sum

    Sales_Analysis.objects.create(
        earnings=sum
    )

    return None

