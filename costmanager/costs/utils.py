from django.db.models import Q
from .models import Product

def searchProducts(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    products = Product.objects.distinct().filter(
        Q(nume_produs__icontains=search_query) |
        Q(pret__icontains=search_query) |
        Q(descriere__icontains=search_query)
    )
    return products, search_query