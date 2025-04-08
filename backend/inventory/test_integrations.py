from rest_framework.test import APISimpleTestCase, APIClient
from mongoengine.context_managers import switch_db
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from . import views
import json


class APITest(APISimpleTestCase):
    def setUp(self):
        self.client = APIClient()
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Product.objects.all().delete()
        Category.objects.all().delete()
        cls.prod=[]
        cls.cat=[]
        for i in range(10):
            pc=[]
            for pr in cls.prod:
                pc.append(pr.id)
            p = Product(name=f"prod{i}",brand=f"brand{i}",description=f"desc{i}",price=i*3+0.1,quantity=i*10)
            cls.prod.append(p)
            c = Category(name=f"cat{i}",description=f"desc{i}",products=pc)
            cls.cat.append(c)
            p.save()
            c.save()
        
            
    def test_prod_list(self):
        response = self.client.get("/inventory/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data),len(Product.objects.all()))
        
        
    def test_prod_get(self):
        response = self.client.get(f"/inventory/products/{self.prod[3].pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'],"prod3")
        
    def test_prod_create(self):
        size = len(Product.objects.all())
        response = self.client.post(f"/inventory/products",data={"name":"prod10","brand":"brand10"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Product.objects.all()),size+1)
        
    def test_prod_delete(self):
        size = len(Product.objects.all())
        response = self.client.delete(f"/inventory/products/{self.prod[5].pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Product.objects.all()),size-1)
        
    def test_prod_update(self):
        self.assertEqual(self.prod[0]['name'],"prod0")
        data = {"name":"updated0"}
        response = self.client.patch(f"/inventory/products/{str(self.prod[0].pk)}",data=data,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"],"updated0")
    
    
    def test_cat_list(self):
        response = self.client.get("/inventory/categories")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data),len(Category.objects.all()))
        
    def test_cat_get(self):
        response = self.client.get(f"/inventory/categories/{self.cat[3].pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'],"cat3")
        
    def test_cat_create(self):
        size = len(Category.objects.all())
        response = self.client.post(f"/inventory/categories",data={"name":"cat10","description":"desc10"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Category.objects.all()),size+1)
        
    def test_cat_delete(self):
        size = len(Category.objects.all())
        response = self.client.delete(f"/inventory/categories/{self.cat[5].pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Category.objects.all()),size-1)
        
    def test_cat_update(self):
        self.assertEqual(self.cat[0]['name'],"cat0")
        data = {"name":"updated0"}
        response = self.client.patch(f"/inventory/categories/{str(self.cat[0].pk)}",data=data,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"],"updated0")
        
    def test_cat_get_prod(self):
        response = self.client.get(f"/inventory/categories/{str(self.cat[1].pk)}/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data),len(self.cat[1].products))
        
    def test_cat_add_prod(self):
        size = len(self.cat[1].products)
        response = self.client.post(f"/inventory/categories/{str(self.cat[1].pk)}/products/{str(self.prod[1].pk)}")
        self.assertEqual(response.status_code, 201)
        self.cat[1].reload()
        self.assertEqual(len(self.cat[1].products),size+1)
        
    def test_cat_del_prod(self):
        size = len(self.cat[1].products)
        response = self.client.delete(f"/inventory/categories/{str(self.cat[1].pk)}/products/{str(self.prod[0].pk)}")
        self.assertEqual(response.status_code, 204)
        self.cat[1].reload()
        self.assertEqual(len(self.cat[1].products),size-1)
        
    # failing cases    
    
    def test_prod_list_fail(self):
        response = self.client.get("/inventory/product")
        self.assertEqual(response.status_code, 404)
        
        
    def test_prod_get_fail(self):
        response = self.client.get(f"/inventory/products/12345678910111213141516171")
        self.assertEqual(response.status_code, 404)
                
    def test_prod_create_fail(self):
        response = self.client.post(f"/inventory/products",data={"name":"prod10"})
        self.assertEqual(response.status_code, 400)
        
    def test_prod_delete_fail(self):
        response = self.client.delete(f"/inventory/products/12345678910111213141516171")
        self.assertEqual(response.status_code, 400)
        
    def test_prod_update_fail(self):
        self.assertEqual(self.prod[0]['name'],"prod0")
        data = {"name":"updated0","brand":None}
        response = self.client.patch(f"/inventory/products/{str(self.prod[0].pk)}",data=data,format='json')
        self.assertEqual(response.status_code, 400)
    
    
    def test_cat_list_fail(self):
        response = self.client.get("/inventory/categorie")
        self.assertEqual(response.status_code, 404)
        
    def test_cat_get_fail(self):
        response = self.client.get(f"/inventory/categories/12345678910111213141516171")
        self.assertEqual(response.status_code, 404)
        
    def test_cat_create_fail(self):
        response = self.client.post(f"/inventory/categories",data={"name":"","description":"desc10"})
        self.assertEqual(response.status_code, 400)
        
    def test_cat_delete_fail(self):
        response = self.client.delete(f"/inventory/categories/12345678910111213141516171")
        self.assertEqual(response.status_code, 400)
        
    def test_cat_update_fail(self):
        data = {"name":"updated0"}
        response = self.client.patch(f"/inventory/categories/12345678910111213141516171",data=data,format='json')
        self.assertEqual(response.status_code, 400)
        
    def test_cat_get_prod_fail(self):
        response = self.client.get(f"/inventory/categories/{str(self.cat[1].pk)}/product")
        self.assertEqual(response.status_code, 404)
        
    def test_cat_add_prod_fail(self):
        response = self.client.post(f"/inventory/categories/{str(self.cat[1].pk)}/products/{str(self.prod[1].pk)}")
        self.assertEqual(response.status_code, 400)
        
    def test_cat_del_prod_fail(self):
        response = self.client.delete(f"/inventory/categories/{str(self.cat[1].pk)}/products/{str(self.prod[6].pk)}")
        self.assertEqual(response.status_code, 400)
