from django_rest1.celery import app
from .models import Emails, Liked_Product
from .service import *


@app.task
def send_email(email):
    send(email)


@app.task
def sending_delayed_emails():
    emails = Emails.objects.all()
    if emails:
        for email in emails:
            send(email)


@app.task
def delete_liked_product():
    last_month = get_last_month()
    Liked_Product.objects.filter(date__gte=last_month)
    lps = Liked_Product.objects.all()
    for lp in lps:
        lp.delete()
