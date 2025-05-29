from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_products, name="favoriteproducts"),
    path('product/<str:pk>/', views.product, name='product'),
    path('monthlycosts/', views.costs_per_month, name="costs_per_month"),
    path('favoriteshops/', views.favorite_shops, name="favoriteshops"),

    path('add-product/', views.add_product, name='add-product'),

    path('update-product/<str:pk>/', views.update_product, name='update-product'),

    path('delete-product/<str:pk>/', views.delete_product, name='delete-product'),
]