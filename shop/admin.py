
from typing import Dict, Optional, Tuple
from django.contrib import admin
from django.http.request import HttpRequest
from parler.admin import TranslatableAdmin
from . models import Category, Product

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}

    def get_prepopulated_fields(
            self, 
            request: HttpRequest, 
            obj:None = None) -> Dict[str, Tuple[str]]:
        return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug':('name',)}

    def get_prepopulated_fields(
            self, 
            request: HttpRequest, 
            obj:None = None) -> Dict[str, Tuple[str]]:
        return {'slug': ('name',)}