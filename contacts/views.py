from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import response,status
# Create your views here.


class ContactListView(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class ContactDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field="id"


    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)