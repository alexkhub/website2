from rest_framework import serializers

from .models import *
from shop.models import Products, Product_Images


#вспомогательные сериализаторы
class FilterImagesSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(first_img=True)
        return super().to_representation(data)

# class FilterUnpaidOrdersSerializer(serializers.ListSerializer):
#
#     def to_representation(self, data):
#         print(data)
#         data = data.filter(paid_order=False)
#         data = data.filter(delivery=False)
#
#         return super().to_representation(data)
#
#
#
# class Id_Unpaid_OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = '__all__'
#         list_serializer_class = FilterUnpaidOrdersSerializer


class ProductMainImagesListSerializer(serializers.ModelSerializer):
    '''вывод главной картинки '''
    class Meta:
        model = Product_Images
        fields = ('img',)
        list_serializer_class = FilterImagesSerializer





# сериализаторы отрисовки страниц

class Order_Point_ProductSerializer(serializers.ModelSerializer):
    ''''создание вложенного сериализатора'''
    product_photos = ProductMainImagesListSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = ('product_name', 'description', 'product_photos')
        read_only = ('owner.username',)


class Order_PointsSerializer(serializers.ModelSerializer):
    #серилизатор для вывода пунктов корзины
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    product = Order_Point_ProductSerializer(many=False, read_only=True)
    # если у нас 1 объект писать many= False

    class Meta:
        model = Order_Points
        fields = '__all__'


class Unpaid_OrderSerializer(serializers.ModelSerializer):
    # id = Id_Unpaid_OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'
        read_only= True

    # def to_representation(self, instance):
    #     data = super(Unpaid_OrderSerializer, self).to_representation(instance)
    #     print(data)
    #     data = data.filter(paid_order=False)
    #     data = data.filter(delivery=False)
    #     return data

