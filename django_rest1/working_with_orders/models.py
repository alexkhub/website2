from django.db import models

from sortedm2m.fields import SortedManyToManyField

from shop.models import Products, Users, Transactions


# Create your models here.

class Order_Points(models.Model):
    user = models.ForeignKey('shop.Users', on_delete=models.PROTECT, verbose_name='Пользователь')
    product = models.ForeignKey('shop.Products', on_delete=models.PROTECT, verbose_name='Продукт')

    amount = models.IntegerField(verbose_name='Количество', default=1)
    price = models.IntegerField(verbose_name='Цена', blank=True)
    in_orders = models.BooleanField(verbose_name='Участвует в заказе ', default=False, blank=True)

    def __str__(self):
        return f"пользователель {self.user} продукт {self.product}"

    def save(self, *args, **kwargs):
        if not self.in_orders:
            amount = self.amount
            product = Products.objects.get(product_name=self.product)
            product_price = float(product.last_price)
            self.price = product_price * amount
        super(Order_Points, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пункт заказа"
        verbose_name_plural = "Пункты заказов"


class Payment_Method(models.Model):
    name = models.CharField(max_length=50, verbose_name="Способ оплаты", unique=True)
    discount = models.FloatField(verbose_name="Доп проценты")
    description = models.TextField(verbose_name="Условия")
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Метод оплаты"
        verbose_name_plural = "Методы оплаты"


class Orders(models.Model):
    user = models.ForeignKey('shop.Users', on_delete=models.PROTECT, verbose_name='Пользователь')
    order_points = SortedManyToManyField(Order_Points, verbose_name="Пункт заказа")
    payment_method = models.ForeignKey("Payment_Method", on_delete=models.PROTECT, verbose_name="Способ оплаты")
    delivery = models.BooleanField(default=False, verbose_name="Доставка")
    price = models.FloatField(blank=True, verbose_name='Цена заказа')
    paid_order = models.BooleanField(default=False, verbose_name='Оплачен')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Время заказа")

    # def save(self, *args, **kwargs):
    # payment_method = Payment_Method.objects.get(name=self.payment_method)
    # payment_method_discount = payment_method.discount
    # price_orders_points = 0
    # for order_point in self.order_points.all():
    #     price_orders_points += order_point.price
    # price = price_orders_points
    # if payment_method_discount > 0:
    #     price = price * (1 + payment_method_discount / 100)
    # if self.delivery:
    #     price += 300
    # self.price = price
    # super(Orders, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"пользователь-{self.user} заказ-{self.id}"


class Paid_Orders(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.PROTECT, verbose_name='Заказ')
    transactions = models.ForeignKey('shop.Transactions', on_delete=models.PROTECT, verbose_name='Транзакция')
    date = models.DateTimeField(verbose_name="Дата заказа", auto_now_add=True)

    class Meta:
        verbose_name = 'Оплаченный заказ'
        verbose_name_plural = 'Оплаченные заказы'

    def __str__(self):
        return self.id


# class Cancelled_Orders(models.Model):
#     order = models.ForeignKey('Orders', on_delete=models.PROTECT, verbose_name='Заказ')
#     reason = models.TextField(verbose_name="Причина", blank=True)
#
#     class Meta:
#         verbose_name = 'Отмененный заказ'
#         verbose_name_plural = 'Отменные заказы'
#
#
# class Installments(models.Model):
#     order = models.ForeignKey('Orders', on_delete=models.PROTECT, verbose_name='Заказ')
#     payment_per_month = models.FloatField(verbose_name='Месячная плата')
#     transactions = SortedManyToManyField(Transactions, verbose_name='Транзакции')
#
#     class Meta:
#         verbose_name = 'Заказ с рассрочкой'
#         verbose_name_plural = 'Заказы с рассрочкой'


class Orders_With_Delivery(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.PROTECT, verbose_name='Заказ')
    condition = models.BooleanField(verbose_name='Состояние', default=False)

    class Meta:
        verbose_name = 'Заказ с доставкой'
        verbose_name_plural = 'Заказы с доставкой'

    def __str__(self):
        return self.id
