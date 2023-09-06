from rest_framework import serializers

from .models import *
from shop.models import Products, Product_Images


#вспомогательные сериализаторы
class FilterImagesSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(first_img=True)
        return super().to_representation(data)




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

    class Meta:
        model = Orders
        fields = ('id', 'date')
        read_only= True


