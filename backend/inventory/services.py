from .serializers import ProductSerializer
from .serializers import CategorySerializer
from .repository import CategoryRepository
from .repository import ProductRepository

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
        
class CategoryService():
    def list_all(rep):
        res = rep.list_all()
        ser = CategorySerializer(res,many=True)
        return ser.data
    
    def create(rep,data):
        ser = CategorySerializer(data=data,partial=True)
        if ser.is_valid():
            try:
                res = rep.create(ser.validated_data)
                ser = CategorySerializer(res)
                return ser.data
            except Exception as e:
                raise ValidationError(e)
        else:
            raise ValidationError(ser.errors)
    
    def get(rep,pk):
        try:
            res = rep.get(pk)
            ser = CategorySerializer(res)
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
            ser = CategorySerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
        
    def list_prod(rep,pk):
        try:
            res = rep.list_prod(pk)
            ser = ProductSerializer(res,many=True)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
    
    def add_prod(rep,pk,ppk):
        try:
            prod = ProductRepository().get(ppk)
            rep.add_prod(pk,prod)
        except Exception as e:
            raise ValidationError(e)
            
    def del_prod(rep,pk,ppk):
        try:
            prod = ProductRepository().get(ppk)
            rep.del_prod(pk,prod)
        except Exception as e:
            raise ValidationError(e)
        