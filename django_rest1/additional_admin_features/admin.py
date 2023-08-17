from django.contrib import admin

from .models import *


class Products_Sales_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'date', 'amount', 'earnings')
    list_display_links = ('id', 'product',)

    search_fields = ('id', 'product', 'date')
    list_filter = ('product', 'date', 'amount', 'earnings')

class Categorys_Sales_AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'date', 'amount', 'earnings')
    list_display_links = ('id', 'category',)

    search_fields = ('id', 'category', 'date')
    list_filter = ('category', 'date', 'amount', 'earnings')

admin.site.register(Products_Sales_Analysis, Products_Sales_AnalysisAdmin)
admin.site.register(Categorys_Sales_Analysis, Categorys_Sales_AnalysisAdmin)