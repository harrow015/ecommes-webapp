from django.db import models

# Create your models here.
class customer_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Place=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20,default='null')
    
    
class cart_tb(models.Model):
    productid=models.ForeignKey('shop.product_tb',on_delete=models.CASCADE)
    customer_id=models.ForeignKey(customer_tb,on_delete=models.CASCADE)
    shipping_address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    quantity=models.IntegerField()
    total=models.IntegerField()

class order_table(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    customer_id=models.ForeignKey(customer_tb,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='pending')
    order_date=models.CharField(max_length=20)
    order_time=models.CharField(max_length=20)
    grandtotal=models.IntegerField()
    
class oderitems_table(models.Model):
    order_id=models.ForeignKey(order_table,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(customer_tb,on_delete=models.CASCADE)
    productid=models.ForeignKey('shop.product_tb',on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()        
    
    
    
class payment_tb(models.Model):
    cardname=models.CharField(max_length=20)
    cardnumber=models.CharField(max_length=20)
    cvv=models.CharField(max_length=20)
    expiary_date=models.CharField(max_length=20) 
    customer_id=models.ForeignKey(customer_tb,on_delete=models.CASCADE)
    orderid=models.ForeignKey(order_table,on_delete=models.CASCADE)      
