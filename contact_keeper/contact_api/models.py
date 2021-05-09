from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=80, blank=True)
    phone = models.IntegerField()
    type = models.CharField(max_length=20)


