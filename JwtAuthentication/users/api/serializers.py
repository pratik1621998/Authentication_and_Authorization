from rest_framework import serializers
from users.models import *

#------------------- USER REGISTRATION SERIALIZER -----------------#

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ["id", "first_name","password", "password2", "last_name", "email", "role","is_active", "is_staff", "is_admin", "created_at", "updated_at"]

        extra_kwargs = {
            'password' : {'write_only': True},
        }

    def create(self, validated_data):
        validated_data["role"] = 2
        
        return User.objects.create_user(**validated_data)
    

#------------------ LOGIN USER REGISTRATION ---------------------#

class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ["email", "password"]
