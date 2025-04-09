from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, 'templates/login_register.html')