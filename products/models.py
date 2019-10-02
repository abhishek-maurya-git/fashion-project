from django.db import models

class Products(models.Model):
    name = models.TextField(max_length=100)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    rate = models.IntegerField(default=0)


    def __str__(self):
        return self.name
