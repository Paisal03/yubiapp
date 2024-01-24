from django.urls import path
from user import views
urlpatterns=[
    path("",views.index,name="index"),
    path("createuser/",views.createuser,name="createuser" ),
    path("getuser/",views.getuser,name="getuser"),
    path("login/",views.login,name="login")
    # path("createuser/",views.createuser,name="createuser"),
    # path("login/",views.login,name="login"),
    # path("readfile/",views.readfile,name="getuser")
]