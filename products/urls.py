from django.urls import path
from .views import ProductList, CreateProduct, CategoryList

urlpatterns = [
    path('', ProductList.as_view(), name="products"),
    path("create-product/", CreateProduct.as_view(), name="create-product"), 
    path("categories/", CategoryList.as_view(), name="categories")
]
