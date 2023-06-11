from django.contrib import admin
from .models import *


class Order_PointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'price')
    list_display_links = ('product', 'user')
    list_filter = ('product', 'user')
    search_fields = ('product', 'user')

class Payment_MethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount')
    list_display_links = ('name', 'discount')
    prepopulated_fields = {'slug': ('name',)}


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_method', 'get_order_points', 'delivery', 'price', 'date' )
    list_display_links = ('id', 'user', 'payment_method', )
    search_fields = ('id', 'user')
    list_filter = ('payment_method',  'delivery', 'price', 'date')
    list_editable = ('delivery',)

    @admin.display(description='пункты заказа')
    def get_order_points(self, obj):
        return [order_point.pk for order_point in obj.order_points.all()]




admin.site.register(Order_Points, Order_PointsAdmin)
admin.site.register(Payment_Method, Payment_MethodAdmin)
admin.site.register(Orders, OrdersAdmin)