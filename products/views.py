from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import ProductForm
from .models import Product

# Create your views here.
def created_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()

    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)

    return render(request, 'products/product_list.html', {'products': products})

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/delete_product.html', {'product': product})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})