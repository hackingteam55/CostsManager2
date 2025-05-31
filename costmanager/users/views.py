from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, ShopForm
from .utils import searchProfiles

# Create your views here.

def profiles(request):
    profiles, search_query = searchProfiles(request)

    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles.html', context)

@login_required(login_url="login")
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user_profile.html', context)


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request,'Username or password is incorrect!')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Cont creat cu succes')

            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'Eroare de inregistrare')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile

    products = profile.product_set.all()

    context = {'profile': profile, 'products': products}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def addShop(request):
    profile = request.user.profile
    form = ShopForm

    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.owner = profile
            shop.save()
            messages.success(request, 'Magazin adaugat cu succes')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/shop_form.html', context)
