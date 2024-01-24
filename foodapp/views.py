from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Category, FoodItem
from .serializers import CategorySerializer, FoodItemSerialize

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodItemList(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


    def get_queryset(self):
        is_vegetarian = self.request.query_params.get('is_vegetarian', None)
        queryset = FoodItem.objects.all()
        
        if is_vegetarian is not None:
            is_vegetarian = is_vegetarian.lower() == 'true'
            queryset = queryset.filter(is_vegetarian=is_vegetarian)

        return queryset  
    

    def get_queryset(self):
        allowed_name = "payas"
        return FoodItem.objects.filter(name=allowed_name)