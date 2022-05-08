from urllib import response
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
# Create your views here.


class RegisterView(GenericAPIView):
    authentication_classes=[]

    serializer_class=UserSerializer

    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(GenericAPIView):
    authentication_classes=[]
    
    serializer_class=LoginSerializer

    def post(self,request):
        username=request.data.get('username',None)
        password=request.data.get('password',None)
        
        user=auth.authenticate(username=username,password=password)

        if user:
            token=jwt.encode({"username":user.username},settings.JWT_SECRET_KEY)
            serializer=self.serializer_class(user)
            data={"user":serializer.data,"token":token}
            return Response(data,status=status.HTTP_200_OK)
        return Response({"message":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        