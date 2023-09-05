from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from users.manager import *
import uuid
import datetime

#-------------------------- USER MODEL ----------------------#

class User(AbstractBaseUser, PermissionsMixin):

    SUPERADMIN = 0 
    ADMIN = 1
    USER = 2

    ROLE_CHOICES = (
        (SUPERADMIN, 'Superadmin'),
        (ADMIN, 'Admin'),
        (USER, 'User'),
    )

    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank= True, null= True, default=2)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    
