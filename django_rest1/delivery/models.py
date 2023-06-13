from django.db import models
from sortedm2m.fields import SortedManyToManyField
from working_with_orders.models import Orders_With_Delivery
from shop.models import Users
# Create your models here.\

class Cars(models.Model):
    car_number = models.CharField(verbose_name='Номер машины', unique=True, max_length=30)
    car_brand =  models.CharField(verbose_name='Номер машины', max_length=60)
    payload = models.IntegerField(verbose_name='Грузоподъемность', default=1500)

    def __str__(self):
        return self.car_number

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Delivery(models.Model):
    worker = models.ForeignKey('shop.Users', on_delete=models.PROTECT , verbose_name="Сотрудник")
    orders = SortedManyToManyField(Orders_With_Delivery, verbose_name='Заказы')
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Машина')
    date = models.DateField(verbose_name='Дата' , auto_now_add=True)

    def __str__(self):
        return f"{self.worker}-{self.car}-{self.date}"

    class Meta:
        verbose_name = 'Заказ на день'
        verbose_name_plural = 'Заказы на день'



