# Generated by Django 4.2.1 on 2023-06-06 13:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], max_length=1, verbose_name='Пол')),
                ('phone', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Телефон')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/%Y/%m/%d/', verbose_name='Аватарки')),
                ('description', models.TextField(blank=True, verbose_name='О себе')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория продукта',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=100, unique=True, verbose_name='Наименование производителя')),
                ('country', models.CharField(blank=True, max_length=40, verbose_name='Страна')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, db_index=True, max_length=70, unique=True, verbose_name='Название продукта')),
                ('first_price', models.FloatField(verbose_name='Первоначальная цена')),
                ('discount', models.FloatField(blank=True, default=0, verbose_name='Скидка')),
                ('last_price', models.FloatField(blank=True, verbose_name='Конечная  цена')),
                ('numbers', models.IntegerField(verbose_name='Количество продуктов')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='О продукте')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукция',
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='Product_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(blank=True, max_length=50, verbose_name='Картинка изображения')),
                ('img', models.ImageField(upload_to='img_product/%Y/%m/%d/', verbose_name='Изображение продукта')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Фотография продукта',
                'verbose_name_plural': 'Фотографии продуктов',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(default=0, verbose_name='Сумма')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Начало скидок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotions_name', models.CharField(blank=True, db_index=True, max_length=70, unique=True, verbose_name='Название акции')),
                ('price', models.FloatField(verbose_name='Цена акции')),
                ('discount_start_date', models.DateField(auto_now_add=True, verbose_name='Начало скидок')),
                ('discount_end_date', models.DateField(verbose_name='Конец скидок')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='img_product/%Y/%m/%d/', verbose_name='Картинка акции')),
                ('products', sortedm2m.fields.SortedManyToManyField(help_text=None, to='shop.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукция',
                'ordering': ['promotions_name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_photos',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='shop.product_images', verbose_name='Изображения'),
        ),
        migrations.CreateModel(
            name='Discount_For_Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.FloatField(verbose_name='Скидка')),
                ('discount_start_date', models.DateField(auto_now_add=True, verbose_name='Начало скидок')),
                ('discount_end_date', models.DateField(verbose_name='Конец скидок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('category_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория товаров')),
            ],
            options={
                'verbose_name': 'Скидка на категорию продукта',
                'verbose_name_plural': 'Скидки на категории продуктов',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Комментарий')),
                ('rating', models.FloatField(verbose_name='Оценка от 1 до 10 ')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Продукты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['rating'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.manufacturer', verbose_name='Производитель'),
        ),
    ]
