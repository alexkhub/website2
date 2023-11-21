from django.core.mail import send_mail
from datetime import date, timedelta
from PIL import Image, ImageDraw
from django_filters import rest_framework as filters
from .models import Products, Category, Manufacturer
from django.core.cache import cache

from django_rest1 import settings


def update_photo(img):
    size = (200, 200)
    original = Image.open(img)
    original.thumbnail(size)
    mask = Image.new('L', original.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, original.width, original.height), fill=255)
    result = Image.new('RGBA', original.size)
    result.paste(original, (0, 0), mask=mask)
    return result


def send(user_email):
    send_mail(
        'Добро пожаловать',
        'Мы будем присылать вам QR код ',
        'aleksandrkhubaevwork@gmail.com',
        [user_email],
        fail_silently=False
    )


def yesterday():
    day = date.today()
    day_before = day - timedelta(days=1)
    return day_before


def get_last_month():
    day = date.today()
    last_month = day - timedelta(weeks=4, days=3)
    return last_month


def get_categories():
    category_cache = cache.get(settings.CATEGORIES_CACHE)
    if category_cache:
        categories = category_cache
    else:
        categories = Category.objects.all().only('slug', 'category_photo', 'name')
        cache.set(settings.CATEGORIES_CACHE, categories, 60 * 60 * 2)
    return categories


def get_manufacturers():
    manufacturers_cache = cache.get(settings.MANUFACTURERS_CACHE)
    if manufacturers_cache:
        manufacturers = manufacturers_cache
    else:
        manufacturers = Manufacturer.objects.all().only('slug', 'photo', 'manufacturer_name')
        cache.set(settings.MANUFACTURERS_CACHE, manufacturers, 60 * 60 * 2)
    return manufacturers


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    last_price = filters.RangeFilter()
    category = CharFilterInFilter(field_name='category__slug', lookup_expr='in')
    manufacturer = CharFilterInFilter(field_name='manufacturer__slug', lookup_expr='in')
    discount = filters.BooleanFilter(field_name='discount', lookup_expr='gte')

    class Meta:
        model = Products
        fields = ['last_price', 'category', 'manufacturer', 'discount']


class ManufactureFilter(filters.FilterSet):
    last_price = filters.RangeFilter()
    category = CharFilterInFilter(field_name='category__slug', lookup_expr='in')
    discount = filters.BooleanFilter(field_name='discount', lookup_expr='gte')

    class Meta:
        model = Products
        fields = ['last_price', 'category', 'discount']


class CategoryFilter(filters.FilterSet):
    last_price = filters.RangeFilter()
    manufacturer = CharFilterInFilter(field_name='manufacturer__slug', lookup_expr='in')
    discount = filters.BooleanFilter(field_name='discount', lookup_expr='gte')

    class Meta:
        model = Products
        fields = ['last_price', 'manufacturer', 'discount']
