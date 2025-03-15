from django.urls import path,include
from django.http import HttpResponse
from . import views

def temp(request):
    return HttpResponse("Inside inventory")

urlpatterns = [
    path('', views.ProductListAndCreate.as_view()),
    path('<int:pk>/', views.ProductRUD.as_view()),
]