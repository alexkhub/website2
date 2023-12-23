import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest1.settings')

app = Celery('django_rest1')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
# response = app.control.enable_events(reply=True)

app.conf.beat_schedule = {
    'send-spam-email': {
        'task': 'additional_admin_features.tasks.send_spam',
        'schedule': crontab(minute='0', hour='12')
    },
    'analysis': {
        'task': ['sales_analysis'],
        'schedule': crontab(minute='30', hour='0')
    },
    'sending_delayed_emails':{
        'task': 'shop.tasks.sending_delayed_emails',
        'schedule': crontab(hour='12')

    },
    'delete_liked_product': {
        'task': 'shop.tasks.delete_liked_product',
        'schedule': crontab(hour='1', minute='30')

    },
    'update_amount': {
        'task': 'company_orders.tasks.update_amount',
        'schedule': crontab(minute='*/60')
    }

}
