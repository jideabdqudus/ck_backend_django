from django.shortcuts import render
from .models import Contacts
from rest_framework import viewsets, permissions
from .serializers import ContactSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ContactSerializer

    def get_queryset(self):
        """Returns Contacts for the user"""
        return self.request.user.contacts.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
