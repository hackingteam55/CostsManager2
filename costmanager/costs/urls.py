from django.urls import path
from . import views

urlpatterns = [
    path('monthlycosts/', views.costs_per_month, name="costs_per_month"),
    path('favoriteproducts', views.favorite_products, name="favoriteproducts"),
    path('favoriteshops', views.favorite_shops, name="favoriteshops")
]