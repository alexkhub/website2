# Generated by Django 4.2.1 on 2023-07-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_comments_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='gender',
        ),
    ]
