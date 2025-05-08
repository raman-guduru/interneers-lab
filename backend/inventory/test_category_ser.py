import unittest
from unittest.mock import Mock

from .services import CategoryService
from .models import Category, Product
from .repository import CategoryRepository,ProductRepository



class TestCategoryService(unittest.TestCase):
    def setUp(self):
        self.CatRep = Mock()
        self.ProdRep = Mock()
    # for good cases
    def test_list_all(self):
        self.CatRep.list_all.return_value = [Category(name='test1',description='description1')]
        res = CategoryService(self.ProdRep,self.CatRep).list_all()
        self.assertEqual(res,[{"id":None,"name":"test1","description":"description1"}])
        
    def test_create(self):
        self.CatRep.create.return_value = Category(name='test1',description='description1')
        res = CategoryService(self.ProdRep,self.CatRep).create({'name':'test1','description':'description1'})
        self.assertEqual(res,{"id":None,"name":"test1","description":"description1"})
        
    def test_get(self):
        self.CatRep.get.return_value = Category(name='test1',description='description1')
        res = CategoryService(self.ProdRep,self.CatRep).get('blah-blah')
        self.assertEqual(res,{"id":None,"name":"test1","description":"description1"})
        
    def test_delete(self):
        self.CatRep.delete.return_value = None
        res = CategoryService(self.ProdRep,self.CatRep).delete('blah-blah')
        self.assertIsNone(res)
        
    def test_update(self):
        self.CatRep.get.return_value = Category(name='test1',description='description1')
        self.CatRep.update.return_value = {"id":None,"name":"test-updated","description":None,"description":"description1","price":None,"quantity":None}
        res = CategoryService(self.ProdRep,self.CatRep).update('blah-blah',{"name":"test-updated"})
        self.assertEqual(res,{"id":None,"name":"test-updated","description":"description1"})
        
    def test_list_prod(self):
        self.CatRep.list_prod.return_value = [Product(name='prod1',brand='brand1')]
        res = CategoryService(self.ProdRep,self.CatRep).list_prod('blah-blah')
        self.assertEqual(res,[{"id":None,"name":"prod1","description":None,"brand":"brand1","price":None,"quantity":None}])
        
    def test_add_prod(self):
        self.ProdRep.get = Mock(return_value = Product(name='prod1',brand='brand1'))
        self.CatRep.return_value.add_prod.return_value = None
        self.assertIsNone(CategoryService(self.ProdRep,self.CatRep).add_prod('blah-blah','blah..'))
        
    def test_del_prod(self):
        self.ProdRep.get = Mock(return_value = Product(name='prod1',brand='brand1'))
        self.CatRep.return_value.del_prod.return_value = None
        self.assertIsNone(CategoryService(self.ProdRep,self.CatRep).del_prod('blah-blah','blah..'))
    
    
    # for bad cases
    def test_list_fail(self):
        self.CatRep.list_all.side_effect = Exception("blah..")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).list("blah-blah")
    
    def test_create_fail(self):
        self.CatRep.create.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).create({'name':'test1'})
        
    def test_get_fail(self):
        self.CatRep.get.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).get("blah-blah")
        
    def test_delete_fail(self):
        self.CatRep.delete.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).delete("blah-blah")
        
    def test_update_fail(self):
        self.CatRep.get.return_value = Category(name='test1',description='description1')
        self.CatRep.update.side_effect = Exception("blah-blah")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).update({'name':"blah-blah"})
    
    def test_list_prod_fail(self):
        self.CatRep.list_prod.side_effect = Exception("blah...")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).add_prod("blah-blah")
        
    def test_add_prod_fail(self):
        self.ProdRep.get.return_value = Product(name='prod1',brand='brand1')
        self.CatRep.add_prod.side_effect = Exception("blah..")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).add_prod("blah-blah","blah...")
        
    def test_del_prod_fail(self):
        self.ProdRep.get.return_value = Product(name='prod1',brand='brand1')
        self.CatRep.del_prod.side_effect = Exception("blah..")
        with self.assertRaises(Exception):
            res = CategoryService(self.ProdRep,self.CatRep).del_prod("blah-blah","blah...")
    
if __name__ == "__main__":
    unittest.main()