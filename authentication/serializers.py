from tkinter import TRUE
from urllib import request
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65,min_length=6,write_only=True)
    email = serializers.EmailField(max_length=65,min_length=6)
    first_name = serializers.CharField(max_length=65,min_length=3)
    last_name = serializers.CharField(max_length=65,min_length=3)

    class Meta:
        model=User
        fields =['username','first_name','last_name','email','password']

    def validate(self, attrs):
        email=attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email":('Email already taken')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    
class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=25,min_length=6,write_only=True)
    
    class Meta:
        model=User
        fields=['username','password']
       