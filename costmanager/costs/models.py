import uuid

from django.db import models

# Create your models here.

class Product(models.Model):
    nume = models.CharField(max_length=20)
    magazin = models.CharField(max_length=20, null=True, blank=False)
    pret = models.FloatField(max_length=5, null=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4(), unique=True, primary_key=True, editable=False)


class Shop(models.Model):
    nume = models.CharField(max_length=20)
    locatie = models.CharField(max_length=20)
    orar = models.CharField(max_length=20)



class Cost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
