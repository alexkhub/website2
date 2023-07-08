from rest_framework import serializers

from .models import *


# вспомогательные сериализаторы
class FilterImagesSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(first_img=True)
        return super().to_representation(data)


# сериализаторы отрисовки страниц

class ProductMainImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = ('img', 'first_img', 'img_name')
        list_serializer_class = FilterImagesSerializer

class ProductsListSerializer(serializers.ModelSerializer):
    """сериализатор для вывода продуктов"""
    product_photos = ProductMainImagesListSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        read_only = ('owner.username',)
        fields = '__all__'




class CategoryListSerializer(serializers.ModelSerializer):
    """сериализатор для вывода категорий"""

    class Meta:
        model = Category
        fields = '__all__'


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ('date',)

    def create(self, validated_data):
        comment = Comments.objects.update_or_create(
            user=validated_data.get('user', None),
            product=validated_data.get('product', None),
            defaults={'text': validated_data.get('text'), 'rating': validated_data.get('rating')}
        )
        return comment


class CommentSerializer(serializers.ModelSerializer):
    """сериализатор для вывода комментариев """

    class Meta:
        model = Comments
        fields = ('user', 'text', 'rating', 'date')


class ProductDetailSerializer(serializers.ModelSerializer):
    """сериализатор для вывода продукта"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    product_photos = serializers.SlugRelatedField(slug_field='img_name', read_only=True, many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Products
        read_only = ('owner.username',)
        exclude = ('description', 'slug', 'numbers')


class TestSerializer(serializers.ModelSerializer):
    product_photos = ProductMainImagesListSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
