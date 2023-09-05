from django.contrib import admin
from django.urls import  path

from users.api.views import *

urlpatterns = [

    #------------------- CREATE USER -------------------#
    path('user-create', CreateUserAPI.as_view(), name= "CreateUserAPI"),

    #-------------------- LOGIN USER -------------------#
    path('login-user', LoginUserAPI.as_view(), name="LoginUserAPI"),

    #-------------------- LOGIN ADMIN -------------------#
    path('login-admin', LoginAdminAPI.as_view(), name="LoginAdminAPI"),

    #-------------------- LOGIN SUPERADMIN -------------------#
    path('login-superadmin', LoginSuperAdminAPI.as_view(), name="LoginSuperAdminAPI"),
]