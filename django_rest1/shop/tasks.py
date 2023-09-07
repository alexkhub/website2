from django_rest1.celery import app
from .models import Emails
from .service import *

@app.task
def send_email(email):
    send(email)


@app.task
def sending_delayed_emails():
    emails = Emails.objects.all()
    for email in emails:
        send(email)
        print(email)
        email.delete()
