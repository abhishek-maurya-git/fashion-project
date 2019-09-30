from django.shortcuts import render
from .models import Products

def index(request):
    products = Products.objects
    return render(request,'products/index.html', {'products':products})
