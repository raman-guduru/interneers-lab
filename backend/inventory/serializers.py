from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    brand = serializers.CharField(required=True)
    price = serializers.DecimalField(allow_null=True,max_digits=10,decimal_places=2)
    quantity = serializers.IntegerField(allow_null=True)
    
class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()