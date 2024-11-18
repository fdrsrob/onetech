from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def list_products(request):
    return render(request, 'frontend/showProducts.html')