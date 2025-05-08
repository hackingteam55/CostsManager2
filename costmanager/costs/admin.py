from django.contrib import admin

# Register your models here.
from .models import Product, Shop, Cost

admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Cost)