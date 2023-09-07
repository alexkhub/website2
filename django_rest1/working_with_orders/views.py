from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .serializers import *
from .models import *
from django.db.models import Q
from shop.models import Products


class BasketListView(LoginRequiredMixin, ListAPIView):
    queryset = Order_Points.objects.filter(in_orders=False)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'working_with_orders/basket.html'
    serializer_class = Order_PointsSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializers = Order_PointsSerializer(queryset.filter(user=request.user), many=True)
        return Response(
            {
                'order_points': serializers.data
            }
        )

@login_required(login_url='login')
def order_point_remove(request, id):
    url = request.META.get('HTTP_REFERER')
    order_point = Order_Points.objects.get(id= id)
    user = request.user
    if order_point.user == user:
        order_point.delete()
        return redirect(url)
    else:
        return redirect("home")

class Unpaid_Orders(APIView):
    def get(self, request):
        queryset = Orders.objects.filter(
            Q(user=request.user) & Q(paid_order=False) & Q(delivery = False)
                                         )
        serializers = Unpaid_OrderSerializer(queryset, many=True)
        return Response(serializers.data)
