from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from sortedm2m.fields import SortedManyToManyField


class Users(AbstractUser):
    Gender = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    gender = models.CharField(max_length=1, verbose_name="Пол", choices=Gender, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', )
    birthday = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', verbose_name='Аватарки', blank=True)
    description = models.TextField(verbose_name="О себе", blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Transactions(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Пользователь", blank=True)
    sum = models.IntegerField(verbose_name='Сумма', default=0)
    transaction_date = models.DateTimeField(verbose_name='Начало скидок', auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'




class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100, verbose_name="Наименование производителя", unique=True)
    country = models.CharField(max_length=40, verbose_name='Страна', blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Category(models.Model):
    name = models.CharField(max_length=60, db_index=True, verbose_name="Название категории", )
    description = models.TextField(verbose_name="Описание", blank=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, null=True, verbose_name='Производитель')
    full_name = models.CharField(max_length=100, unique=True, verbose_name="Полное наименование", blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        name = self.name
        manufacturers = Manufacturer.objects.get(manufacturer_name = self.manufacturer)
        self.full_name = f"{name}-{str(manufacturers.manufacturer_name)}"
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'


class Discount_For_Product_Category(models.Model):
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория товаров',
                                      blank=True)
    discount_percentage = models.FloatField(verbose_name='Скидка')
    discount_start_date = models.DateField(verbose_name='Начало скидок', auto_now_add=True)
    discount_end_date = models.DateField(verbose_name='Конец скидок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Скидка на категорию продукта'
        verbose_name_plural = 'Скидки на категории продуктов'


class Product_Images(models.Model):
    img_name = models.CharField(max_length=50, verbose_name='Картинка изображения', blank=True)
    img = models.ImageField(upload_to='img_product/%Y/%m/%d/', verbose_name='Изображение продукта')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.img_name

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'


class Products(models.Model):
    product_name = models.CharField(max_length=70, verbose_name='Название продукта', unique=True, blank=True,
                                    db_index=True)
    first_price = models.FloatField(verbose_name='Первоначальная цена')
    discount = models.FloatField(verbose_name='Скидка', default=0, blank=True)
    last_price = models.FloatField(verbose_name='Конечная  цена', blank=True)
    numbers = models.IntegerField(verbose_name='Количество продуктов')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='URL', )
    description = models.TextField(verbose_name="О продукте", blank=True)
    product_photos = SortedManyToManyField(Product_Images, verbose_name='Изображения')

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('home', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        discount = self.discount
        first_price = self.first_price
        if discount > 0:
            self.last_price = first_price * (1 - discount / 100)
        else:
            self.last_price = first_price

        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
        ordering = ['product_name']


class Comments(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name="Продукты", related_name='comments')
    text = models.TextField(verbose_name="Комментарий", blank=True)
    rating = models.FloatField(verbose_name='Оценка от 1 до 10 ')
    date = models.DateTimeField(verbose_name='Время', auto_now_add=True)


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['rating']



