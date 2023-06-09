# Generated by Django 4.2.1 on 2023-06-30 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('working_with_orders', '0001_initial'),
        ('delivery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='orders',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='working_with_orders.orders_with_delivery', verbose_name='Заказы'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник'),
        ),
    ]
