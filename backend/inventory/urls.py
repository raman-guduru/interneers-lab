from django.urls import path,include
from django.http import HttpResponse
from . import views

def temp(request):
    return HttpResponse("Inside inventory")

urlpatterns = [
    path('', views.ProductLC),
    path('<str:pk>/', views.ProductRUD),
]