from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

# from .models import FoodItem
from food.models import Category
from food.models import FoodItem

def index(request):
    print(request.POST)
    param=dict(request.POST)


    name=str(param["name"][0])
    Category=str(param['name'][0])
    price=str(param['name'][0])


    FoodItem.objects.create(name=name,Category=Category,price=price)

    require_http_methods("succesfully ordered")

def index1(request):
    print(request.GET)

    return HttpResponse ("Hi")




 
 
