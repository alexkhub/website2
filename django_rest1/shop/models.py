from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from sortedm2m.fields import SortedManyToManyField
from autoslug import AutoSlugField


class Users(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    slug = AutoSlugField(populate_from='username', unique=True, db_index=True, verbose_name='URL', )
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    mailing_list = models.BooleanField(default=False, blank=True, verbose_name='Рассылка')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес', null=True)
    user_photo = models.ImageField(upload_to='user_photo/%Y/%m/%d/', verbose_name='Аватарка', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Characteristic(models.Model):
    characteristic_name = models.CharField(max_length=30, verbose_name='Название характеристки')
    value = models.CharField(max_length=20, verbose_name='Значение')

    def __str__(self):
        return f"{self.characteristic_name} {self.value}"

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристи товаров'


class Transactions(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Пользователь", blank=True)
    sum = models.IntegerField(verbose_name='Сумма', default=0)
    transaction_date = models.DateTimeField(verbose_name='Дата транзакции', auto_now_add=True)

    def __str__(self):
        return f'Пользователь {self.user} дата {self.transaction_date}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100, verbose_name="Наименование производителя", unique=True)
    country = models.CharField(max_length=40, verbose_name='Страна', blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )
    photo = models.ImageField(upload_to='img_category/%Y/%m/%d/', verbose_name='Фотография',
                              default='shop/static/img/favicon.svg')

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Category(models.Model):
    name = models.CharField(max_length=60, db_index=True, verbose_name="Название категории", )
    description = models.TextField(verbose_name="Описание", blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', )
    category_photo = models.ImageField(upload_to='img_category/%Y/%m/%d/', verbose_name='Изображение категории')

    def __str__(self):
        return self.name

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
    img_name = models.CharField(max_length=50, verbose_name='Название', blank=True)
    img = models.ImageField(upload_to='img_product/%Y/%m/%d/', verbose_name='Изображение продукта')
    first_img = models.BooleanField(default=False, verbose_name='Главная картинка')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.img_name

    def save(self, *args, **kwargs):
        if self.first_img:
            self.img_name = f'{self.img_name}-main'
            self.slug = f'{self.slug}-main'
        super(Product_Images, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'


class Products(models.Model):
    product_name = models.CharField(max_length=70, verbose_name='Название продукта', unique=True, blank=True,
                                    db_index=True)
    first_price = models.IntegerField(verbose_name='Первоначальная цена')
    discount = models.FloatField(verbose_name='Скидка', default=0, blank=True)
    last_price = models.IntegerField(verbose_name='Конечная  цена', blank=True, null=True)
    numbers = models.IntegerField(verbose_name='Количество продуктов')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='URL', )
    description = models.TextField(verbose_name="О продукте", blank=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, null=True, verbose_name='Производитель',
                                     related_name='manufacturer')
    product_photos = SortedManyToManyField(Product_Images, verbose_name='Изображения', related_name='images',
                                           blank=True, )
    product_characteristic = SortedManyToManyField(Characteristic, verbose_name='Характеристики',
                                                   related_name='characteristics', blank=True, )

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('home', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        if self.discount > 0:
            self.last_price = int(self.first_price * (1 - self.discount / 100))
        else:
            self.last_price = self.first_price
        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
        ordering = ['product_name']


class Comments(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name="Продукты", related_name='comments')
    text = models.TextField(verbose_name="Комментарий", blank=True)
    rating = models.IntegerField(verbose_name='Оценка от 1 до 10 ')
    date = models.DateField(verbose_name='Время', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['rating']


class Emails(models.Model):
    email = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Неоправленное письмо'
        verbose_name_plural = 'Неоправленные письма'


class Liked_Product(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey("Products", on_delete=models.CASCADE, verbose_name="Продукт")
    slug = models.SlugField(verbose_name="URL", unique=True, blank=True)
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.user}-{self.product}-{self.date}"

    def save(self, *args, **kwargs):

        self.slug = f"{self.user} {self.product}"
        super(Liked_Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Понравившийся продукты'
        verbose_name_plural = 'Понравившиеся продукты'
