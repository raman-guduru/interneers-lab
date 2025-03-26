from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import json
# from .services import ProductService
from .models import Product
from .services import ProductService
from .repository import ProductRepository


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