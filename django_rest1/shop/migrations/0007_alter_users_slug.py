# Generated by Django 4.2.1 on 2023-07-14 13:51

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_users_avatar_remove_users_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='username', unique=True, verbose_name='URL'),
        ),
    ]
