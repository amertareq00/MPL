from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'info.html')

def add(request):
    return render(request, 'add.html')

