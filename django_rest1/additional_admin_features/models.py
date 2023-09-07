from django.db import models

from shop.models import Products , Category
# Create your models here.

class Products_Sales_Analysis(models.Model):
    product = models.ForeignKey(Products , on_delete=models.PROTECT, verbose_name='Название продукта')
    amount = models.IntegerField(default=0, verbose_name='Количество проданнах товаров')
    earnings = models.IntegerField(default=0, verbose_name='Прибыль')
    avg_rating = models.FloatField(default=0, verbose_name='Средний рейтинг')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'Продукт-{self.product} {self.date}'

    class Meta:
        verbose_name = "Анализ продажи продукта "
        verbose_name_plural = "Анализ продаж продуктов"


class Categorys_Sales_Analysis(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Название продукта')
    amount = models.IntegerField(default=0, verbose_name='Количество проданнах товаров')
    earnings = models.IntegerField(default=0, verbose_name='Прибыль')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'Категория-{self.category} {self.date}'

    class Meta:
        verbose_name = "Анализ категории "
        verbose_name_plural = "Анализ категорий"

class Sales_Analysis(models.Model):
    earnings = models.IntegerField(default=0, verbose_name='Прибыль')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'Прибыль на {self.date}'

    class Meta:
        verbose_name = 'Прибыль'
        verbose_name_plural = "Прибыль"

class Users_Analysis(models.Model):
    unique_visitors = models.IntegerField(default=0, verbose_name='Уникальные посетители')
    new_user = models.IntegerField(default=0, verbose_name='Новые пользователи')
    delete_user = models.IntegerField(default=0, verbose_name='Удаленные пользователи')
    subscriber = models.IntegerField(default=0, verbose_name='Пользователи с рассылкой')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Анализ пользователелей'
        verbose_name_plural = 'Анализ пользователелей'

    def __str__(self):
        return f'Анализ пользователей на {self.date}'





class Orders_Analysis(models.Model):
    count_paid_orders = models.IntegerField(default=0, verbose_name='Число обычных заказов')
    count_paid_orders_with_delivery = models.IntegerField(default=0, verbose_name='Заказы с доставкой')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Анализ заказов'
        verbose_name_plural = 'Анализ заказов'

    def __str__(self):
        return f'Анализ заказов на {self.date}'

