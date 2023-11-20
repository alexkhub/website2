from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .serializers import *
from .models import *
from django.db.models import Prefetch

from shop.models import Users, Products, Product_Images


class BasketListView(LoginRequiredMixin, ListAPIView):
    queryset = Order_Points.objects.filter(in_orders=False)
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'working_with_orders/basket.html'
    serializer_class = Order_PointsSerializer

    # lookup_field = 'slug'

    def get_queryset(self):
        self.queryset = self.queryset.filter(user=self.request.user).prefetch_related(
            Prefetch('product', queryset=Products.objects.all().prefetch_related(
                Prefetch('product_photos', queryset=Product_Images.objects.filter(first_img=True)
                         .only('img', 'first_img', 'img_name')))
                     .only('id', 'numbers', 'product_photos', 'discount', 'product_name', 'description',
                           'last_price', )
                     ),
            Prefetch('user', queryset=Users.objects.all().only('slug')),
        )
        return self.queryset

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            # {
            #     'order_points': serializer.data
            # }
            serializer.data
        )


class Order_Details(RetrieveAPIView):
    queryset = Orders.objects.all().prefetch_related(
        Prefetch('payment_method', queryset=Payment_Method.objects.all().only('name')),
        Prefetch('order_points',
                 queryset=Order_Points.objects.all().only('id', 'price', 'amount', 'product', ).prefetch_related(
                     Prefetch('product', queryset=Products.objects.all().only('product_name'))
                 ))
    )
    serializer_class = Order_DetailsSerializer
    lookup_field = 'id'


@login_required(login_url='login')
def order_point_remove(request, id):
    url = request.META.get('HTTP_REFERER')
    order_point = Order_Points.objects.get(id=id)
    user = request.user
    if order_point.user == user:
        order_point.delete()
        return redirect(url)
    else:
        return redirect("home")


class BasketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order_Points.objects.filter(in_orders=False)
    serializer_class = Order_PointsSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
