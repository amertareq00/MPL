from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm

def index(request):
    return render(request, 'info.html')

def add(request):
    return render(request, 'add.html')

def addproduct(request):
    if 'product_count' not in request.session:
        request.session['product_count'] = 0

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            request.session['product_count'] += 1
            return redirect('product')
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form, 'product_count': request.session['product_count']})