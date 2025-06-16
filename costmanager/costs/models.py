import uuid
from django.db.models import CASCADE
from django.db import models
import datetime
today = datetime.date.today()
from users.models import Profile
# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    nume_produs = models.CharField(max_length=20)
    nume_magazin = models.ManyToManyField('Shop')
    descriere = models.CharField(default='', max_length=50)
    producator = models.CharField(default='', max_length=50)
    calorii = models.IntegerField(default=0, null=False, blank=False)
    pret = models.FloatField(max_length=5, null=False)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    product_image = models.ImageField(null=True, blank=True, default="no_image.png")

    def __str__(self):
        return self.nume_produs


class Shop(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    nume_magazin = models.CharField(max_length=100, null=False)
    locatie = models.CharField(max_length=100)
    orar = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nume_magazin



class Cost(models.Model):
    luna = models.CharField(default=today.month, max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    total_costuri = models.IntegerField(default=0, null=True, blank=False)


    def __str__(self):
        months = ['zero', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
        current_month = months[today.month]
        return current_month

