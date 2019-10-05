from django.shortcuts import render,get_object_or_404
from .models import Products, Women_products, Kids_products

def index(request):
    products = Products.objects
    return render(request,'products/index.html', {'products':products})

def details(request,product_id):
    product = get_object_or_404(Products,pk=product_id)
    return render(request, 'products/details.html', {'product':product})

def women(request):
    products = Women_products.objects
    return render(request, 'products/w_products.html', {'products':products})

def w_details(request,product_id):
    product = get_object_or_404(Women_products,pk=product_id)
    return render(request, 'products/details.html', {'product':product})