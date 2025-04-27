from django.urls import path,include
from django.http import HttpResponse

from . import views


urlpatterns = [
    path('products', views.ProductLC),
    path('products/<str:pk>', views.ProductRUD),
    path('categories', views.CategoryLC),
    path('categories/<str:pk>', views.CategoryRUD),
    path('categories/<str:pk>/products', views.CategoryListProd),
    path('products/<str:pk>/categories', views.ProductListCategory),
    path('categories/<str:pk>/products/<str:ppk>', views.CategoryAddDelProd),
]