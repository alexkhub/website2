from django.contrib import admin

from .models import *


class Products_Sales_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'date', 'amount', 'avg_rating', 'earnings')
    list_display_links = ('id', 'product',)

    search_fields = ('id', 'product', 'date')
    list_filter = ('product', 'date', 'amount', 'avg_rating', 'earnings')

class Categorys_Sales_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'date', 'amount', 'earnings')
    list_display_links = ('id', 'category',)

    search_fields = ('id', 'category', 'date')
    list_filter = ('category', 'date', 'amount', 'earnings')

class Sales_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'date',  'earnings')
    list_display_links = ('id', )
    search_fields = ('date',)
    list_filter = ('date',  'earnings')

class User_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'unique_visitors', 'new_user', 'delete_user', 'subscriber','date' )
    list_display_links = ('id',)
    search_fields = ('date',)
    list_filter = ('unique_visitors', 'new_user')


class Orders_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'count_paid_orders', 'count_paid_orders_with_delivery', 'date')
    list_display_links = ('id',)
    search_fields = ('date',)



admin.site.register(Products_Sales_Analysis, Products_Sales_AnalysisAdmin)
admin.site.register(Categorys_Sales_Analysis, Categorys_Sales_AnalysisAdmin)
admin.site.register(Sales_Analysis, Sales_AnalysisAdmin)
admin.site.register(Users_Analysis, User_AnalysisAdmin)
admin.site.register(Orders_Analysis, Orders_AnalysisAdmin)