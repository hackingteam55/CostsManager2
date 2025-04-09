from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    page = 'Home'
    return render(request, 'home.html', {'page': page})

def login_view(request):
    page = 'Login/Register'
    return render(request, 'login_register.html', {page: page})