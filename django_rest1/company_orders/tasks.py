from django_rest1.celery import app
from .models import *
from shop.models import Products
from .service import *


@app.task
def update_amount():
    orders = Company_Orders.objects.filter(date=yesterday())
    for order in orders:
        product = Products.objects.get(id=order.product.id)
        product.numbers += order.numbers_of_product
        product.save()
