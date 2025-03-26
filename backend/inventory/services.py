from .serializers import ProductSerializer
from rest_framework.exceptions import ValidationError

class ProductService():
    def list_all(rep):
        res = rep.list_all()
        ser = ProductSerializer(res,many=True)
        return ser.data
    
    def create(rep,data):
        ser = ProductSerializer(data=data,partial=True)
        if ser.is_valid():
            try:
                res = rep.create(ser.validated_data)
                ser = ProductSerializer(res)
                return ser.data
            except Exception as e:
                raise ValidationError(e)
        else:
            raise ValidationError(ser.errors)
    
    def get(rep,pk):
        try:
            res = rep.get(pk)
            ser = ProductSerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
        
    def delete(rep,pk):
        try:
            res = rep.get(pk)
            res = rep.delete(res)
        except Exception as e:
            raise ValidationError(e)
        
    def update(rep,pk,data):
        try:
            res = rep.get(pk)
            res = rep.update(res,data)
            ser = ProductSerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)