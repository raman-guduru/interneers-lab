from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .services import ProductService
from .repository import ProductRepository

from .services import CategoryService
from .repository import CategoryRepository


@api_view(["GET","POST"])
def ProductLC(request):
    service = ProductService(ProductRepository(),CategoryRepository())
    if request.method == "GET":
        try:
            res = service.list_all()
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    else:
        try:
            res = service.create(request.data)
            return Response(status='201',data=res)
        except ValidationError as e:
            return Response(e.detail,status='400')
            
@api_view(["GET","PATCH","DELETE"])
def ProductRUD(request,pk):
    service = ProductService(ProductRepository(),CategoryRepository())
    if request.method == "GET":
        try:
            res = service.get(pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    elif request.method == "DELETE":
        try:
            res = service.delete(pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
    else:
        try:
            res = service.update(pk,request.data)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
        

@api_view(["GET","POST"])
def CategoryLC(request):
    service = CategoryService(ProductRepository(),CategoryRepository())
    if request.method == "GET":
        try:
            res = service.list_all()
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    else:
        try:
            res = service.create(request.data)
            return Response(status='201',data=res)
        except ValidationError as e:
            return Response(e.detail,status='400')
            
@api_view(["GET","PATCH","DELETE"])
def CategoryRUD(request,pk):
    service = CategoryService(ProductRepository(),CategoryRepository())
    if request.method == "GET":
        try:
            res = service.get(pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    elif request.method == "DELETE":
        try:
            res = service.delete(pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
    else:
        try:
            res = service.update(pk,request.data)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
        
@api_view(["GET"])
def CategoryListProd(request,pk):
    service = CategoryService(ProductRepository(),CategoryRepository())
    try:
        res = service.list_prod(pk)
        return Response(data=res,status='200')
    except ValidationError as e:
        return Response(e.detail,status='404')
    
@api_view(["POST","DELETE"])
def CategoryAddDelProd(request,pk,ppk):
    service = CategoryService(ProductRepository(),CategoryRepository())
    if request.method == "POST":
        try:
            res = service.add_prod(pk,ppk)
            return Response(data=res,status='201')
        except ValidationError as e:
            return Response(e.detail,status='400')
    else:
        try:
            res = service.del_prod(pk,ppk)
            return Response(data=res,status='204')
        except ValidationError as e:
            return Response(e.detail,status='400')
        
@api_view(["GET"])
def ProductListCategory(request,pk):
    service = CategoryService(ProductRepository(),CategoryRepository())
    try:
        res = service.has_prod(pk)
        return Response(data=res,status='200')
    except ValidationError as e:
        return Response(e.detail,status='404')