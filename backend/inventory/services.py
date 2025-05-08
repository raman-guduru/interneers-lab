from .serializers import ProductSerializer
from .serializers import CategorySerializer
from .repository import CategoryRepository
from .repository import ProductRepository

from rest_framework.exceptions import ValidationError

class ProductService():
    def __init__(self,ProdRep,CatRep):
        self.ProdRep = ProdRep
        self.CatRep = CatRep
        
    def list_all(self):
        res = self.ProdRep.list_all()
        ser = ProductSerializer(res,many=True)
        return ser.data
    
    def create(self,data):
        ser = ProductSerializer(data=data,partial=True)
        if ser.is_valid():
            try:
                res = self.ProdRep.create(ser.validated_data)
                ser = ProductSerializer(res)
                return ser.data
            except Exception as e:
                raise ValidationError(e)
        else:
            raise ValidationError(ser.errors)
    
    def get(self,pk):
        try:
            res = self.ProdRep.get(pk)
            ser = ProductSerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
        
    def delete(self,pk):
        try:
            res = self.ProdRep.get(pk)
            res = self.ProdRep.delete(res)
        except Exception as e:
            raise ValidationError(e)
        
    def update(self,pk,data):
        try:
            res = self.ProdRep.get(pk)
            res = self.ProdRep.update(res,data)
            ser = ProductSerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
        
class CategoryService():
    def __init__(self,ProdRepo,CatRepo):
        self.ProdRepo = ProdRepo
        self.CatRepo = CatRepo
    
    def list_all(self):
        res = self.CatRepo.list_all()
        print(res)
        ser = CategorySerializer(res,many=True)
        return ser.data
    
    def create(self,data):
        ser = CategorySerializer(data=data,partial=True)
        if ser.is_valid():
            try:
                res = self.CatRepo.create(ser.validated_data)
                ser = CategorySerializer(res)
                return ser.data
            except Exception as e:
                raise ValidationError(e)
        else:
            raise ValidationError(ser.errors)
    
    def get(self,pk):
        try:
            res = self.CatRepo.get(pk)
            ser = CategorySerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
        
    def delete(self,pk):
        try:
            res = self.CatRepo.get(pk)
            res = self.CatRepo.delete(res)
        except Exception as e:
            raise ValidationError(e)
        
    def update(self,pk,data):
        try:
            res = self.CatRepo.get(pk)
            res = self.CatRepo.update(res,data)
            ser = CategorySerializer(res)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
        
    def list_prod(self,pk):
        try:
            res = self.CatRepo.list_prod(pk)
            ser = ProductSerializer(res,many=True)
            return ser.data
        except Exception as e:
            raise ValidationError(e)
    
    def add_prod(self,pk,ppk):
        try:
            prod = self.ProdRepo.get(ppk)
            self.CatRepo.add_prod(pk,prod)
        except Exception as e:
            raise ValidationError(e)
            
    def del_prod(self,pk,ppk):
        try:
            prod = self.ProdRepo.get(ppk)
            self.CatRepo.del_prod(pk,prod)
        except Exception as e:
            raise ValidationError(e)
        
    def has_prod(self,pk):
        product = self.ProdRepo.get(pk)
        res = self.CatRepo.has_prod(product)
        ser = CategorySerializer(res,many=True)
        return ser.data
        