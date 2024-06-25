from django.db import models

# Create your models here.

class shop_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    
class product_tb(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(max_length=20)
    price = models.CharField(max_length=20)
    details = models.CharField(max_length=20)
    stock = models.IntegerField()
    shop_id = models.ForeignKey(shop_tb,on_delete=models.CASCADE)    
