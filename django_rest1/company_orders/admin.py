from django.contrib import admin
from .models import *


# Register your models here.
class Company_OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product', 'manufacturer', 'price_of_1_product', 'numbers_of_product', 'discount', 'total_price', 'date')
    list_display_links = ('id', 'product',)
    list_filter = ('manufacturer', 'price_of_1_product', 'numbers_of_product', 'discount', 'total_price', 'date')
    search_fields = ('product', 'manufacturer', 'date')


admin.site.register(Company_Orders, Company_OrdersAdmin)
