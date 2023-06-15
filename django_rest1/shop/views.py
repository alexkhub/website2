from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .models import *
from .serializers import *


class ProductsListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/home.html'

    def get(self, request):

        products = Products.objects.filter(discount=0)  # товары без скидки
        products_with_discount = Products.objects.filter(discount__gt=0)  # товары со скидкой
        serializer = ProductsListSerializer(products, many=True)
        return Response(
            {'serializer': serializer, 'products': products, 'products_with_discount': products_with_discount})


class ProductDetailView(APIView):

    def get(self, request, product_slug):

        products = Products.objects.get(slug = product_slug)  # товары без скидки

        serializer = ProductsListSerializer(products)
        return Response(serializer.data)