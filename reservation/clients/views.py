from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm

def index(request):
    return render(request, 'info.html')

def add(request):
    return render(request, 'add.html')

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process the form data (save to database, etc.) if needed
            # For now, just render the template with the form data
            return render(request, 'product.html', {'form': form})
    else:
        form = ProductForm()

    return render(request, 'product.html', {'form': form})