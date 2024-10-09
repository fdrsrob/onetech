from django.urls import path
from .views import user_list, user_create, user_edit, user_details, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', user_create, name='user_create'),
    path('edit/<int:pk>/', user_edit, name='user_edit'),
    path('details/<int:pk>/', user_details, name='user_details'),
    path('delete/<int:pk>/', user_delete, name='user_delete'),
]