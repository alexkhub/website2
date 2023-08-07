from django_rest1.celery import app

from .service import *

@app.task
def send_email(email):
    send(email)