from .models import Product
from .models import Category

class ProductRepository():
    def list_all(self):
        return Product.objects.all()
    
    def create(self,data):
        ins = Product(**data)
        ins.save()
        return ins
    
    def get(self,pk):
        try:
            ins = Product.objects.get(pk=pk)
            return ins
        except Product.DoesNotExist:
            raise Exception("Product not found")
    
    def update(self,ins,data):
        ins.update(**data)
        ins.reload()
        return ins
        
    def delete(self,ins):
        ins.delete()
        
    def save(self,ins):
        ins.save()

class CategoryRepository():
    def list_all(self):
        return Category.objects.all()
    
    def create(self,data):
        ins = Category(**data)
        ins.save()
        return ins
    
    def get(self,pk):
        try:
            ins = Category.objects.get(pk=pk)
            return ins
        except Category.DoesNotExist:
            raise Exception("Category not found")
    
    def update(self,ins,data):
        ins.update(**data)
        ins.reload()
        return ins
        
    def delete(self,ins):
        ins.delete()
        
    def list_prod(self,pk):
        try:
            ins = Category.objects.get(pk=pk)
            return ins.products
        except Category.DoesNotExist:
            raise Exception("Category not found")
        
    def add_prod(self,pk,prod):
        try:
            ins = Category.objects.get(pk=pk)
            if prod in ins.products:
                raise Exception("Product already in category")
            else:
                ins.modify(push__products=prod)
        except Category.DoesNotExist:
            raise Exception("Category not found")
        
    def del_prod(self,pk,prod):
        try:
            ins = Category.objects.get(pk=pk)
            if prod not in ins.products:
                raise Exception("Product not in category")
            else:
                ins.modify(pull__products=prod)
        except Category.DoesNotExist:
            raise Exception("Category not found")