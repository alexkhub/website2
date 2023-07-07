from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_login', 'username', 'email', 'gender', 'phone', 'is_staff')
    list_display_links = ('id', 'last_login', 'username', 'email', 'phone',)
    prepopulated_fields = {"slug": ("username",)}
    search_fields = ('id', 'username', 'phone', 'email')
    list_filter = ('is_staff',)
    list_editable = ('is_staff',)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sum', 'transaction_date')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'transaction_date')
    prepopulated_fields = {"slug": ('user', 'sum', 'transaction_date')}


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name', 'country')
    list_display_links = ('manufacturer_name',)
    search_fields = ('manufacturer_name', 'country')
    list_filter = ('country',)
    prepopulated_fields = {"slug": ("manufacturer_name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ('name', )


class Discount_For_Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'discount_percentage', 'discount_start_date', 'discount_end_date')
    list_display_links = ('id',)
    search_fields = ('category_name', 'discount_start_date', 'discount_end_date')
    list_filter = ('category_name', 'discount_start_date', 'discount_end_date')
    prepopulated_fields = {'slug': ('category_name', 'discount_start_date', 'discount_end_date')}
    list_editable = ('discount_end_date',)


class Product_ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_name', 'first_img','get_image')
    readonly_fields = ('get_image',)
    list_display_links = ('img_name',)
    prepopulated_fields = {'slug': ('img_name',)}
    search_fields = ('img_name',)
    list_editable = ('first_img',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="60" height="60"')

    get_image.short_description = "Изображение продукта"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'first_price', 'last_price', 'numbers', 'discount', 'category', 'manufacturer')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name',)
    list_filter = ('last_price', 'discount', 'category')
    list_editable = ('first_price', 'last_price', 'numbers', 'discount')
    prepopulated_fields = {'slug': ('product_name',)}


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text', 'rating', 'date')
    list_filter = ('rating', 'product')
    search_fields = ('user', 'product')


admin.site.register(Users, UserAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount_For_Product_Category, Discount_For_Product_CategoryAdmin)
admin.site.register(Product_Images, Product_ImagesAdmin)
admin.site.register(Products, ProductAdmin)
admin.site.register(Comments, CommentsAdmin)
