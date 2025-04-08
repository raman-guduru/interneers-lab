# import unittest
# from unittest.mock import Mock

# from .services import ProductService
# from .models import Product

# class TestProductService(unittest.TestCase):
#     def setUp(self):
#         self.rep = Mock()
    
#     # for good cases
#     def test_list_all(self):
#         self.rep.list_all.return_value = [Product(name='test1',brand='brand1')]
#         res = ProductService.list_all(self.rep)
#         self.assertEqual(res,[{"id":None,"name":"test1","description":None,"brand":"brand1","price":None,"quantity":None}])
        
#     def test_create(self):
#         self.rep.create.return_value = Product(name='test1',brand='brand1')
#         res = ProductService.create(self.rep,{'name':'test1','brand':'brand1'})
#         self.assertEqual(res,{"id":None,"name":"test1","description":None,"brand":"brand1","price":None,"quantity":None})
        
#     def test_get(self):
#         self.rep.get.return_value = Product(name='test1',brand='brand1')
#         res = ProductService.get(self.rep,'blah-blah')
#         self.assertEqual(res,{"id":None,"name":"test1","description":None,"brand":"brand1","price":None,"quantity":None})
        
#     def test_delete(self):
#         self.rep.delete.return_value = None
#         res = ProductService.delete(self.rep,'blah-blah')
#         self.assertIsNone(res)
        
#     def test_update(self):
#         self.rep.get.return_value = Product(name='test1',brand='brand1')
#         self.rep.update.return_value = {"id":None,"name":"test-updated","description":None,"brand":"brand1","price":None,"quantity":None}
#         res = ProductService.update(self.rep,'blah-blah',{"name":"test-updated"})
#         self.assertEqual(res,{"id":None,"name":"test-updated","description":None,"brand":"brand1","price":None,"quantity":None})
    
#     # for bad cases
#     def test_list_fail(self):
#         self.rep.list.side_effect = Exception("blah..")
#         with self.assertRaises(Exception):
#             res = ProductService.list(self.rep,"blah-blah")
    
#     def test_create_fail(self):
#         self.rep.create.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = ProductService.create(self.rep,{'name':'test1'})
        
#     def test_get_fail(self):
#         self.rep.get.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = ProductService.get(self.rep,"blah-blah")
        
#     def test_delete_fail(self):
#         self.rep.delete.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = ProductService.delete(self.rep,"blah-blah")
        
#     def test_update_fail(self):
#         self.rep.get.return_value = Product(name='test1',brand='brand1')
#         self.rep.update.side_effect = Exception("blah-blah")
#         with self.assertRaises(Exception):
#             res = ProductService.update(self.rep,{'name':"blah-blah"})
    
# if __name__ == "__main__":
#     unittest.main()