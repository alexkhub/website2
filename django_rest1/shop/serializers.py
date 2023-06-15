from rest_framework import serializers

from .models import *


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        read_only = ('owner.username',)
        fields = ('product_name', 'first_price', 'discount', 'last_price')


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        read_only = ('owner.username',)
        exclude = ('description', 'slug', 'numbers')


