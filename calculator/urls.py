from django.urls import path
from calculator import views

urlpatterns=[
    path("",views.index,name="index"),
    path("add", views.index1, name='addition'),
    path("sub", views.index2, name='substraction'),
    path("multi", views.index3, name='multiplication'),
    path("div", views.index4, name='division'),
]