from itertools import product
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductImage
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer
from rest_framework import status
from rest_framework import generics

from products import serializers

# Create your views here.

class ProductList(APIView):
    """ List all products """

    def get(self,request, category_id, format=None):
        category = get_object_or_404(Category, id=category_id)
        product = Product.objects.filter(category=category)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data) 
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class CreateProduct(generics.CreateAPIView):
    """ Allow product creation """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(APIView):
    """ list all product categories"""
    def get(self):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
class CreateProductImage(generics.CreateAPIView):
    """ posting of product images associated with a specific product"""
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer



