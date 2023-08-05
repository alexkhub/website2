from django_rest1.celery import app

from .service import *

@app.task
def send_emails(mail_text, user_email):
    send(mail_text, user_email)

