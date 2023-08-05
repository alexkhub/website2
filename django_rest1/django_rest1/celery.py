import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest1.settings')

app = Celery('django_rest1')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()