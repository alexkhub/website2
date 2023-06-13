from django.contrib import admin

# Register your models here.
from .models import *


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_number', 'car_brand', 'payload')
    list_display_links = ('id', 'car_number')
    search_fields = ('car_number',)
    list_filter = ('car_brand', 'payload')


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'get_orders', 'car', 'date')
    list_display_links = ('id',  'get_orders')
    list_filter = ('worker', 'car', 'date')

    @admin.display(description='Заказы')
    def get_orders(self, obj):
        return [order.pk for order in obj.orders.all()]


admin.site.register(Cars, CarsAdmin)
admin.site.register(Delivery, DeliveryAdmin)


