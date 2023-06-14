from rest_framework import serializers

from .models import *


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        field = ('product_name', 'first_price', 'discount', 'last_price')
