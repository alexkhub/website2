from django.db import models

from shop.models import Products , Category
# Create your models here.

class Products_Sales_Analysis(models.Model):
    product = models.ForeignKey(Products , on_delete=models.PROTECT, verbose_name='Название продукта')
    amount = models.IntegerField(default=0, verbose_name='Количество проданнах товаров')
    earnings = models.IntegerField(default=0, verbose_name='Прибыль')
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