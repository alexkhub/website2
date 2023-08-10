import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest1.settings')

app = Celery('django_rest1')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
# response = app.control.enable_events(reply=True)

app.conf.beat_schedule = {
    'send-spam-email':{
        'task': 'additional_admin_features.tasks.send_spam',
        'schedule' : crontab(minute='*/5')
    }

}
