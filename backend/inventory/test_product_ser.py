import unittest
from unittest.mock import Mock

from .services import ProductService
from .models import Product

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.ProdRep = Mock()
        self.CatRep = Mock()
    
    # for good cases
    def test_list_all(self):
        self.ProdRep.list_all.return_value = [Product(name='test1',brand='brand1')]
        res = ProductService(self.ProdRep,self.CatRep).list_all()
        self.assertEqual(res,[{"id":None,"name":"test1","description":None,"brand":"brand1","price":None,"quantity":None}])
        
    def test_create(self):
        self.ProdRep.create.return_value = Product(name='test1',brand='brand1')
        res = ProductService(self.ProdRep,self.CatRep).create({'name':'test1','brand':'brand1'})
        self.assertEqual(res,{"id":None,"name":"test1","description":None,"brand":"brand1","price":None,"quantity":None})
        
    def test_get(self):
        self.ProdRep.get.return_value = Product(name='test1',brand='brand1')
        res = ProductService(self.ProdRep,self.CatRep).get('blah-blah')
        self.assertEqual(res,{"id":None,"name":"test1","description":None,"brand":"brand1","price":None,"quantity":None})
        
    def test_delete(self):
        self.ProdRep.delete.return_value = None
        res = ProductService(self.ProdRep,self.CatRep).delete('blah-blah')
        self.assertIsNone(res)
        
    def test_update(self):
        self.ProdRep.get.return_value = Product(name='test1',brand='brand1')
        self.ProdRep.update.return_value = {"id":None,"name":"test-updated","description":None,"brand":"brand1","price":None,"quantity":None}
        res = ProductService(self.ProdRep,self.CatRep).update('blah-blah',{"name":"test-updated"})
        self.assertEqual(res,{"id":None,"name":"test-updated","description":None,"brand":"brand1","price":None,"quantity":None})
    
    # for bad cases
    def test_list_fail(self):
        self.ProdRep.list.side_effect = Exception("blah..")
        with self.assertRaises(Exception):
            res = ProductService(self.ProdRep,self.CatRep).list("blah-blah")
    
    def test_create_fail(self):
        self.ProdRep.create.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = ProductService(self.ProdRep,self.CatRep).create({'name':'test1'})
        
    def test_get_fail(self):
        self.ProdRep.get.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = ProductService(self.ProdRep,self.CatRep).get("blah-blah")
        
    def test_delete_fail(self):
        self.ProdRep.delete.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = ProductService(self.ProdRep,self.CatRep).delete("blah-blah")
        
    def test_update_fail(self):
        self.ProdRep.get.return_value = Product(name='test1',brand='brand1')
        self.ProdRep.update.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = ProductService(self.ProdRep,self.CatRep).update({'name':"blah-blah"})
    
if __name__ == "__main__":
    unittest.main()