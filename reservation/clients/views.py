from django.http import HttpResponse
from .forms import ProductForm
from django.shortcuts import render, redirect
from .forms import ClientTypeForm, ClientForm
from .models import Client


def index(request):
    return render(request, 'info.html')

def add(request):
    return render(request, 'add.html')

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return render(request, 'product.html', {'form': form})
    else:
        form = ProductForm()
#
    return render(request, 'product.html', {'form': form})



def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'add_client.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})