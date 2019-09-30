from django.shortcuts import render,get_object_or_404
from .models import Products

def index(request):
    products = Products.objects
    return render(request,'products/index.html', {'products':products})

def details(request,product_id):
    product = get_object_or_404(Products,pk=product_id)
    return render(request, 'products/details.html', {'product':product})
