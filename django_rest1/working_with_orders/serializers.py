from rest_framework import serializers

from .models import *
from shop.models import Products, Product_Images


# вспомогательные сериализаторы
class ProductImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = ('img', 'first_img', 'img_name')


# сериализаторы отрисовки страниц

class Order_Point_ProductSerializer(serializers.ModelSerializer):
    ''''создание вложенного сериализатора'''
    product_photos = ProductImagesListSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ('product_name', 'description', 'product_photos', 'last_price')
        read_only = ('owner.username',)


class Order_PointsSerializer(serializers.ModelSerializer):
    # серилизатор для вывода пунктов корзины
    user = serializers.CharField(source='user.slug')
    product = Order_Point_ProductSerializer(many=False, read_only=True)

    # если у нас 1 объект писать many= False

    class Meta:
        model = Order_Points
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'date')
        read_only = True


class Order_Details_Order_PointsSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.product_name')

    class Meta:
        model = Order_Points
        fields = ('id', 'price', 'amount', 'product')


class Order_DetailsSerializer(serializers.ModelSerializer):
    payment_method = serializers.CharField(source='payment_method.name', read_only=True)
    order_points = Order_Details_Order_PointsSerializer(many=True)

    class Meta:
        model = Orders
        fields = '__all__'
