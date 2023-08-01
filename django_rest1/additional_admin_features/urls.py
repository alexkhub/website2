from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='additional_admin_features'),
    path('mailing/', MailingForm.as_view(), name='aaf_mailing'),
]