# Generated by Django 4.2.1 on 2023-06-30 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_category_manufacturer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_photos',
            new_name='category_photo',
        ),
    ]
