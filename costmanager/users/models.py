import uuid

from django.db import models

# Create your models here.

class Users(models.Model):
    nume = models.TextField(default='Name', max_length=20)
    prenume = models.TextField(default='Prenume', max_length=20)
    email = models.EmailField(default='email@example.com', max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
