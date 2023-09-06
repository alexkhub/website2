from django.urls import path

from .views import *


urlpatterns = [
    path('', BasketListView.as_view(), name='basket'),
    path('order_point_remove/<int:id>/', order_point_remove, name='order_point_remove'),
    path('unpaid_orders/', Unpaid_Orders.as_view(), name='unpaid_orders')
]