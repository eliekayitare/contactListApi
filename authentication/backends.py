from asyncio import exceptions
import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from django.contrib.auth.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        auth_data=authentication.get_authorization_header(request)

        if not auth_data:
            return None
        prefix,token=auth_data.decode('utf-8').split(' ')

        try:
            payload=jwt.decode(token,settings.JWT_SECRET_KEY,algorithms='HS256')
            user=User.objects.get(username=payload['username'])
            return (user,token)

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed("Token is expired,login again")
        
        except jwt.DecodeError as exc:
            raise exceptions.AuthenticationFailed("Token is Invalid")

        