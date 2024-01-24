from django.urls import path
from .views import CategoryList, FoodItemList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('fooditems/', FoodItemList.as_view(), name='fooditem-list'),
]