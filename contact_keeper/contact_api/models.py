from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=80, blank=True)
    phone = models.IntegerField()
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE, null=True)

