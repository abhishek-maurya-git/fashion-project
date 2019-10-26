from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/', default='')
    image_3 = models.ImageField(upload_to='images/', default='')    
    rate = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Women_products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/', default='')
    image_3 = models.ImageField(upload_to='images/', default='')
    rate = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +" ("+ self.product.name+")"