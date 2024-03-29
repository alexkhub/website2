from abc import ABC

from rest_framework import serializers
from .models import *


# вспомогательные сериализаторы
class FilterImagesSerializer(serializers.ListSerializer, ABC):
    def to_representation(self, data):
        data = data.filter(first_img=True)
        return super().to_representation(data)


# сериализаторы отрисовки страниц

class ProductMainImagesListSerializer(serializers.ModelSerializer):
    """вывод главной картинки """

    class Meta:
        model = Product_Images
        fields = ('img',)
        list_serializer_class = FilterImagesSerializer


class ProductImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = ('img', 'first_img', 'img_name')


class ProductsListSerializer(serializers.ModelSerializer):
    """сериализатор для вывода продуктов"""
    product_photos = ProductImagesListSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    manufacturer = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Products
        read_only = ('owner.username',)
        exclude = ('numbers', 'product_characteristic', 'first_price', 'description',)


class HomeProductsListSerializer(serializers.ModelSerializer):
    """сериализатор для вывода продуктов"""
    product_photos = ProductImagesListSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        read_only = ('owner.username',)
        exclude = ('numbers', 'product_characteristic', 'first_price', 'description', 'manufacturer', 'category')


class CategoryListSerializer(serializers.ModelSerializer):
    """сериализатор для вывода категорий"""

    class Meta:
        model = Category
        fields = ('slug', 'category_photo', 'name')


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """сериализатор для вывода комментариев """
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    """сериализатор для вывода продукта"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    manufacturer = serializers.SlugRelatedField(slug_field='manufacturer_name', read_only=True)
    product_photos = ProductImagesListSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        read_only = ('owner.username',)
        exclude = ('numbers', 'product_characteristic',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        read_only = ('owner.username',)
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'phone', 'address', 'user_photo',)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        read_only = ('owner.username',)
        fields = ("manufacturer_name", "slug", "photo")


class UpdateEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Users
        read_only = ('owner.username',)
        fields = ("email", )

    def update(self, instance, validated_data,):

        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
