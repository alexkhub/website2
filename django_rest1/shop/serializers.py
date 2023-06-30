from rest_framework import serializers

from .models import *


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        read_only = ('owner.username',)
        fields = ('product_name', 'first_price', 'discount', 'last_price',)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


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
    class Meta:
        model = Comments
        fields = ('user', 'text', 'rating', 'date')


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    product_photos = serializers.SlugRelatedField(slug_field='img_name', read_only=True, many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Products
        read_only = ('owner.username',)
        exclude = ('description', 'slug', 'numbers')


