# Generated by Django 4.2.1 on 2023-08-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_with_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_points',
            name='in_orders',
            field=models.BooleanField(blank=True, default=False, verbose_name='Участвует в заказе '),
        ),
    ]
