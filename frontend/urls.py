from django.urls import path
from .views import index, list_products

urlpatterns = [
    path('', index, name='index'),
    path('products/', list_products, name='list_products'),
]