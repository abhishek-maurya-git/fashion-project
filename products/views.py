from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Products, Women_products, Favorite
from django.contrib.auth.decorators import login_required

def index(request):
    products = Products.objects.all
    # favorite = Favorite()
    # favorite.objects.filter(user=request.user).count()
    print('yeah')
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

@login_required(login_url="/accounts/signup")
def fav(request, fav_id):
    product = get_object_or_404(Products, pk=fav_id)
    favorite = Favorite()
    print('before request.user')
    favorite.user = request.user
    favorite.product = product
    print('just before save.')
    favorite.save()
    
    return redirect ('index')
    