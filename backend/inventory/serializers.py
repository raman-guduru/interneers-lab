from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    brand = serializers.CharField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    quantity = serializers.IntegerField()