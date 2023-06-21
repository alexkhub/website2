from rest_framework.response import Response
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status
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
        products = Products.objects.get(slug=product_slug)  # товары без скидки

        serializer = ProductDetailSerializer(products)
        return Response(serializer.data)


class CreateCommentView(APIView):

    def post(self, request):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)

    # def put(self, request, id=None ):
    #     comment = Comments.objects.filter(id=id)
    #     serializer = CreateCommentSerializer(comment, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

