from itertools import product
from django.shortcuts import render
from .models import Product, Category, ProductImage
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import status
from rest_framework import generics

# Create your views here.

class ProductList(APIView):
    """ List all products """

    def get(self, request, format=None):
        product = Product.objects.all()
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



