from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .services import ProductService
from .repository import ProductRepository

from .services import CategoryService
from .repository import CategoryRepository


@api_view(["GET","POST"])
def ProductLC(request):
    rep = ProductRepository()
    if request.method == "GET":
        try:
            res = ProductService.list_all(rep)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    else:
        try:
            res = ProductService.create(rep=rep,data=request.data)
            return Response(status='201',data=res)
        except ValidationError as e:
            return Response(e.detail,status='400')
            
@api_view(["GET","PUT","DELETE"])
def ProductRUD(request,pk):
    rep = ProductRepository()
    if request.method == "GET":
        try:
            res = ProductService.get(rep,pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    elif request.method == "DELETE":
        try:
            res = ProductService.delete(rep,pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
    else:
        try:
            res = ProductService.update(rep,pk,request.data)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
        

@api_view(["GET","POST"])
def CategoryLC(request):
    rep = CategoryRepository()
    if request.method == "GET":
        try:
            res = CategoryService.list_all(rep)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    else:
        try:
            res = CategoryService.create(rep=rep,data=request.data)
            return Response(status='201',data=res)
        except ValidationError as e:
            return Response(e.detail,status='400')
            
@api_view(["GET","PUT","DELETE"])
def CategoryRUD(request,pk):
    rep = CategoryRepository()
    if request.method == "GET":
        try:
            res = CategoryService.get(rep,pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='404')
    elif request.method == "DELETE":
        try:
            res = CategoryService.delete(rep,pk)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
    else:
        try:
            res = CategoryService.update(rep,pk,request.data)
            return Response(data=res,status='200')
        except ValidationError as e:
            return Response(e.detail,status='400')
        
@api_view(["GET"])
def CategoryListProd(request,pk):
    rep = CategoryRepository()
    try:
        res = CategoryService.list_prod(rep,pk)
        return Response(data=res,status='200')
    except ValidationError as e:
        return Response(e.detail,status='404')
    
@api_view(["POST","DELETE"])
def CategoryAddDelProd(request,pk,ppk):
    rep = CategoryRepository()
    if request.method == "POST":
        try:
            res = CategoryService.add_prod(rep,pk,ppk)
            return Response(data=res,status='201')
        except ValidationError as e:
            return Response(e.detail,status='404')
    else:
        try:
            res = CategoryService.del_prod(rep,pk,ppk)
            return Response(data=res,status='204')
        except ValidationError as e:
            return Response(e.detail,status='404')