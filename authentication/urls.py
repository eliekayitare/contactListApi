from django import views
from django.urls import path
from .views import LoginApiView, RegisterView

urlpatterns=[
    path('register',RegisterView.as_view(),name='register'),
    path('login',LoginApiView.as_view(),name='login'),
]