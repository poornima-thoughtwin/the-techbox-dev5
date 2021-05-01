from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions
from django.conf import settings 

User = get_user_model()

class CustomJWTSerializer(TokenObtainPairSerializer):
    

    def validate(self, attrs):
        print("hello1")
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        # This is answering the original question, but do whatever you need here. 
        # For example in my case I had to check a different model that stores more user info
        # But in the end, you should obtain the username to continue.
        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username
            return super().validate(credentials)
            message="not exist user"
        else:
            errmsg = 'My custom error message.'
            message = 200
            #raise ValueError(errmsg)
            raise serializers.ValidationError(
                {"message": "Invailid User"})




class AssetAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAssign
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

