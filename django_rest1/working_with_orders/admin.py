from django.contrib import admin
from .models import *


class Order_PointsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'amount', 'price' , 'in_orders')
    list_display_links = ('product', 'user')
    list_filter = ('product', 'user')
    search_fields = ('product', 'user')
    list_editable = ('in_orders',)


class Payment_MethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount')
    list_display_links = ('name', 'discount')
    prepopulated_fields = {'slug': ('name',)}


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_method', 'get_order_points', 'delivery', 'price', 'date')
    list_display_links = ('id', 'user', 'payment_method',)
    search_fields = ('id', 'user')
    list_filter = ('payment_method', 'delivery', 'price', 'date')
    list_editable = ('delivery',)

    @admin.display(description='пункты заказа')
    def get_order_points(self, obj):
        return [order_point.pk for order_point in obj.order_points.all()]


class Paid_OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'transactions', 'date')
    list_display_links = ('id', 'order', 'transactions', 'date')
    list_filter = ('date',)
    search_fields = ('id', 'order', 'transactions')


# class Cancelled_OrdersAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order',)
#     list_display_links = ('id', 'order',)
#
#
# class InstallmentsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order', 'payment_per_month', 'get_transactions')
#     list_display_links = ('id', 'order', 'payment_per_month', 'get_transactions')
#
#     @admin.display(description='Транзакции')
#     def get_transactions(self, obj):
#         return [transaction.pk for transaction in obj.transactions.all()]


class Orders_With_DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'condition',)
    list_display_links = ('id', 'order', )
    list_editable = ('condition',)


admin.site.register(Order_Points, Order_PointsAdmin)
admin.site.register(Payment_Method, Payment_MethodAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Paid_Orders, Paid_OrdersAdmin)
# admin.site.register(Cancelled_Orders, Cancelled_OrdersAdmin)
# admin.site.register(Installments, InstallmentsAdmin)
admin.site.register(Orders_With_Delivery, Orders_With_DeliveryAdmin)
