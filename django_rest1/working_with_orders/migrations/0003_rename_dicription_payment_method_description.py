# Generated by Django 4.2.1 on 2023-08-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('working_with_orders', '0002_order_points_in_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_method',
            old_name='dicription',
            new_name='description',
        ),
    ]