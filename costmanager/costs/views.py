from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def costs_per_month(request):
    return render(request, 'costs/monthly_costs.html')

def favorite_products(request):
    return render(request, 'costs/favorite_products.html')

def favorite_shops(request):
    return render(request, 'costs/favorite_shops.html')
