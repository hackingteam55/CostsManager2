from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cost, Shop
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .utils import searchProducts


# Create your views here.

@login_required(login_url="login")
def product(request, pk):
    productObj = Product.objects.get(id=pk)
    return render(request, 'costs/single_product.html', {'product': productObj})


def costs_per_month(request):
    monthly_costs = Cost.objects.all()
    context = {'monthly_costs': monthly_costs}
    return render(request, 'costs/monthly_costs.html', context)

@login_required(login_url="login")
def favorite_products(request):
    products, search_query = searchProducts(request)
    context = {'products': products, 'search_query': search_query }
    return render(request, 'costs/favorite_products.html', context)

def favorite_shops(request):
    fav_shop = Shop.objects.all()
    context = {'fav_shop': fav_shop}
    return render(request, 'costs/favorite_shops.html', context)


@login_required(login_url="login")
def add_product(request):
    form  = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('favoriteproducts')

    context = {'form': form}
    return render(request, 'costs/form_product.html', context)


@login_required(login_url="login")
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form  = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('favoriteproducts')

    context = {'form': form}
    return render(request, 'costs/form_product.html', context)


@login_required(login_url="login")
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('favoriteproducts')
    context = {'product': product}
    return render(request, 'costs/delete_template.html', context)
