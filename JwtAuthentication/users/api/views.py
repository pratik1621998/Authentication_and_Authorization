from users.models import *
from users.api.serializers import *
from rest_framework.views import APIView
from core.responses import *
import re
from django.contrib.auth import authenticate
from core.authentication import *


#----------------- CREATE USER API -------------------------#

class CreateUserAPI(APIView):

    def post(self, request):
        data = request.data
        if data["first_name"] != "" and data["last_name"] != "" and data["email"] != "" and data["password"] != "" and data["password2"] != "":
            if re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", data["email"]):
                if data["password"] == data["password2"]:
                    existingUser = User.objects.filter(email = data["email"])
                    if not existingUser:
                        serializer = UserRegistrationSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return onSuccess("User created susccessfully.", serializer.data)
                        else:
                            return badRequest(serializer.errors)
                    else:
                        return badRequest("User already exist with this email address.")
                else:
                    return badRequest("Password and Confirm Password must match.")
            else:
                return badRequest("Invalid Email format.")
        else:
            return badRequest("All the fields are compulsory to fill.")
        

#--------------------------- USER LOGIN --------------------------#

class LoginUserAPI(APIView):

    def post(self, request):
        data = request.data
        if data["email"] != "" and data["password"] != "":
            if re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", data["email"]):
                get_user = User.objects.filter(email = data["email"])
                if get_user:
                    serializer = LoginUserSerializer(data=data)
                    if serializer.is_valid():
                        email = serializer.data.get('email')
                        password = serializer.data.get('password')
                        user = authenticate(email=email, password=password)
                        if user.role == 2:
                            if user is not None:
                                token = create_access_token(user.id)
                                return onSuccess("Login Successful.", token)
                            else:
                                return badRequest("Invalid Credentials.")
                        else:
                            return badRequest("Only User can login.")
                    else: 
                        return badRequest(serializer.errors)
                else:
                    return badRequest("User not found in our system.")
            else:
                return badRequest("Invalid Email format.")
        else:
            return badRequest("All fields are compulsory to fill.")
        

#--------------------------- ADMIN LOGIN --------------------------#

class LoginAdminAPI(APIView):

    def post(self, request):
        data = request.data
        if data["email"] != "" and data["password"] != "":
            if re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", data["email"]):
                get_admin = User.objects.filter(email = data["email"])
                if get_admin:
                    serializer = LoginUserSerializer(data=data)
                    if serializer.is_valid():
                        email = serializer.data.get('email')
                        password = serializer.data.get('password')
                        admin = authenticate(email=email, password=password)
                        if admin.role == 1:
                            if admin is not None:
                                token = create_access_token(admin.id)
                                return onSuccess("Admin Login Successful.", token)
                            else:
                                return badRequest("Invalid Credentials.")
                        else:
                            return badRequest("Only Admin can login.")
                    else: 
                        return badRequest(serializer.errors)
                else:
                    return badRequest("User not found in our system.")
            else:
                return badRequest("Invalid Email format.")
        else:
            return badRequest("All fields are compulsory to fill.")
        

#--------------------------- SUPERADMIN LOGIN --------------------------#

class LoginSuperAdminAPI(APIView):

    def post(self, request):
        data = request.data
        if data["email"] != "" and data["password"] != "":
            if re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", data["email"]):
                get_super_admin = User.objects.filter(email = data["email"])
                if get_super_admin:
                    serializer = LoginUserSerializer(data=data)
                    if serializer.is_valid():
                        email = serializer.data.get('email')
                        password = serializer.data.get('password')
                        superadmin = authenticate(email=email, password=password)
                        if superadmin.role == 0:
                            if superadmin is not None:
                                token = create_access_token(superadmin.id)
                                return onSuccess("Superadmin Login Successful.", token)
                            else:
                                return badRequest("Invalid Credentials.")
                        else:
                            return badRequest("Only Superadmin can login.")
                    else: 
                        return badRequest(serializer.errors)
                else:
                    return badRequest("User not found in our system.")
            else:
                return badRequest("Invalid Email format.")
        else:
            return badRequest("All fields are compulsory to fill.")