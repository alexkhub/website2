from django.urls import path

from .views import *


urlpatterns = [
    path('', BasketListView.as_view(), name='basket'),
    path('order_point_remove/<int:id>/', order_point_remove, name='order_point_remove'),
    path('order_details/<int:id>/', Order_Details.as_view(), name='order_details')
]