from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListAndCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
