from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    Gender = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    gender = models.CharField(max_length=1, verbose_name="Пол", choices=Gender, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', blank=True)
    birthday = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', verbose_name='Аватарки', blank=True)
    description = models.TextField(verbose_name="О себе", blank=True)

    def __str__(self):
        return self.username
