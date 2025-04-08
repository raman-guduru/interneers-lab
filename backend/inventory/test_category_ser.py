# import unittest
# from unittest.mock import Mock, patch

# from .services import CategoryService
# from .models import Category, Product



# class TestCategoryService(unittest.TestCase):
#     def setUp(self):
#         self.rep = Mock()
#     # for good cases
#     def test_list_all(self):
#         self.rep.list_all.return_value = [Category(name='test1',description='description1')]
#         res = CategoryService.list_all(self.rep)
#         self.assertEqual(res,[{"id":None,"name":"test1","description":"description1"}])
        
#     def test_create(self):
#         self.rep.create.return_value = Category(name='test1',description='description1')
#         res = CategoryService.create(self.rep,{'name':'test1','description':'description1'})
#         self.assertEqual(res,{"id":None,"name":"test1","description":"description1"})
        
#     def test_get(self):
#         self.rep.get.return_value = Category(name='test1',description='description1')
#         res = CategoryService.get(self.rep,'blah-blah')
#         self.assertEqual(res,{"id":None,"name":"test1","description":"description1"})
        
#     def test_delete(self):
#         self.rep.delete.return_value = None
#         res = CategoryService.delete(self.rep,'blah-blah')
#         self.assertIsNone(res)
        
#     def test_update(self):
#         self.rep.get.return_value = Category(name='test1',description='description1')
#         self.rep.update.return_value = {"id":None,"name":"test-updated","description":None,"description":"description1","price":None,"quantity":None}
#         res = CategoryService.update(self.rep,'blah-blah',{"name":"test-updated"})
#         self.assertEqual(res,{"id":None,"name":"test-updated","description":"description1"})
        
#     def test_list_prod(self):
#         self.rep.list_prod.return_value = [Product(name='prod1',brand='brand1')]
#         res = CategoryService.list_prod(self.rep,'blah-blah')
#         self.assertEqual(res,[{"id":None,"name":"prod1","description":None,"brand":"brand1","price":None,"quantity":None}])
        
#     @patch("inventory.services.ProductRepository",new_callable=Mock)
#     def test_add_prod(self,MockProductRepository):
#         MockProductRepository.return_value.get.return_value = Product(name='prod1',brand='brand1')
#         self.rep.add_prod.return_value = None
#         self.assertIsNone(CategoryService.add_prod(self.rep,'blah-blah','blah..'))
        
#     @patch("inventory.services.ProductRepository",new_callable=Mock)
#     def test_del_prod(self,MockProductRepository):
#         MockProductRepository.return_value.get.return_value = Product(name='prod1',brand='brand1')
#         self.rep.del_prod.return_value = None
#         self.assertIsNone(CategoryService.del_prod(self.rep,'blah-blah','blah..'))
    
    
#     # for bad cases
#     def test_list_fail(self):
#         self.rep.list.side_effect = Exception("blah..")
#         with self.assertRaises(Exception):
#             res = CategoryService.list(self.rep,"blah-blah")
    
#     def test_create_fail(self):
#         self.rep.create.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = CategoryService.create(self.rep,{'name':'test1'})
        
#     def test_get_fail(self):
#         self.rep.get.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = CategoryService.get(self.rep,"blah-blah")
        
#     def test_delete_fail(self):
#         self.rep.delete.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = CategoryService.delete(self.rep,"blah-blah")
        
#     def test_update_fail(self):
#         self.rep.get.return_value = Category(name='test1',description='description1')
#         self.rep.update.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = CategoryService.update(self.rep,{'name':"blah-blah"})
    
#     def test_list_prod_fail(self):
#         self.rep.list_prod.side_effect = Exception("blah...")
#         with self.assertRaises(Exception):
#             res = CategoryService.add_prod(self.rep,"blah-blah")
        
#     @patch("inventory.services.ProductRepository",new_callable=Mock)
#     def test_add_prod_fail(self,MockProductRepository):
#         MockProductRepository.return_value.get.return_value = Product(name='prod1',brand='brand1')
#         self.rep.add_prod.side_effect = Exception("blah..")
#         with self.assertRaises(Exception):
#             res = CategoryService.add_prod(self.rep,"blah-blah","blah...")
        
#     @patch("inventory.services.ProductRepository",new_callable=Mock)
#     def test_del_prod_fail(self,MockProductRepository):
#         MockProductRepository.return_value.get.return_value = Product(name='prod1',brand='brand1')
#         self.rep.del_prod.side_effect = Exception("blah..")
#         with self.assertRaises(Exception):
#             res = CategoryService.del_prod(self.rep,"blah-blah","blah...")
    
# if __name__ == "__main__":
#     unittest.main()