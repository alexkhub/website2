from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .models import *
from .serializers import *
from rest_framework.status import HTTP_200_OK


class ProductsListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shop/home.html'

    def get(self, request):
        products = Products.objects.filter(discount=0)  # товары без скидки
        products_with_discount = Products.objects.filter(discount__gt=0)  # товары со скидкой
        categories = Category.objects.all()

        products_serializer = ProductsListSerializer(products, many=True)
        products_with_discount_serializer = ProductsListSerializer(products_with_discount, many=True)
        category_serializer = CategoryListSerializer(categories, many=True)

        return Response(
            {'serializer': products_serializer.data,
             'products_with_discount': products_with_discount_serializer.data,
             'category_serializer': category_serializer.data,
             }
        )


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
