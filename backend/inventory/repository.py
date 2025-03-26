from .models import Product

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
            raise Exception("Id not found")
    
    def update(self,ins,data):
        ins.update(**data)
        ins.reload()
        return ins
        
    def delete(self,ins):
        ins.delete()