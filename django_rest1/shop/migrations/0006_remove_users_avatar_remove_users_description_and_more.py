# Generated by Django 4.2.1 on 2023-07-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_users_mailing_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='users',
            name='description',
        ),
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(blank=True, max_length=150, verbose_name='Адрес'),
        ),
    ]