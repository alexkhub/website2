# Generated by Django 4.2.1 on 2023-09-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_users_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='img_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название'),
        ),
    ]