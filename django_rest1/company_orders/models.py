from django.db import models
from shop.models import Products, Manufacturer


class Company_Orders(models.Model):
    product = models.ForeignKey("shop.Products", on_delete=models.PROTECT, verbose_name='Продукт')
    manufacturer = models.ForeignKey("shop.Manufacturer", on_delete=models.PROTECT, verbose_name='Производитель')
    price_of_1_product = models.FloatField(verbose_name="Цена 1 продукта")
    numbers_of_product = models.IntegerField(verbose_name="Количество продуктов")
    discount = models.FloatField(verbose_name="Скидка", default=0)
    total_price = models.FloatField(verbose_name="Общая стоимость", blank=True)
    date = models.DateField(verbose_name="Дата закупки", auto_now_add=True)

    class Meta:
        verbose_name = "Заказ компании"
        verbose_name_plural = "Заказы компании"

    def save(self, *args, **kwargs):
        discount = self.discount
        price_of_1_product = self.price_of_1_product
        numbers_of_product = self.numbers_of_product
        if discount > 0:
            self.total_price = price_of_1_product * numbers_of_product * (1 - discount / 100)
        else:
            self.total_price = price_of_1_product * numbers_of_product

        super(Company_Orders, self).save(*args, **kwargs)
