from django.contrib import admin
from datetime import timedelta
from . models import Category,Product,ProductImage

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock")

class AdminProductImage(admin.ModelAdmin):
    list_display= ("product", "image")

admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(ProductImage, AdminProductImage)


