from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='additional_admin_features'),
]