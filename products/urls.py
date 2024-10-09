from django.urls import path
from .views import created_product, product_list, edit_product, delete_product, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', created_product, name='create_product'),
    path('edit/<int:pk>/', edit_product, name='edit_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),
]