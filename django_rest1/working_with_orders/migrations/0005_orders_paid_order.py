# Generated by Django 4.2.1 on 2023-09-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_with_orders', '0004_remove_installments_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='paid_order',
            field=models.BooleanField(default=False, verbose_name='Оплачен'),
        ),
    ]