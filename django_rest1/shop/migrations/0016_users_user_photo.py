# Generated by Django 4.2.1 on 2023-09-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_users_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_photo/%Y/%m/%d/', verbose_name='Изображение продукта'),
        ),
    ]