# Generated by Django 4.2.1 on 2023-11-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_with_orders', '0007_remove_orders_delivery_remove_orders_paid_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена заказа'),
        ),
    ]
