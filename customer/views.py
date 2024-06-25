
from django.shortcuts import render,redirect
import datetime
from django.contrib import messages
from customer.models import customer_tb
from shop.models import product_tb
from customer.models import cart_tb,order_table,oderitems_table,payment_tb

# Create your views here.
def signup(request):
    return render(request, "signup.html")


def signupaction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    place=request.POST['place']
    username=request.POST['username']
    password=request.POST['password']
    mobile=request.POST['mobile']
    dob=request.POST['dob']
    customer=customer_tb(Name=name,
                         Address=address
                         ,Gender=gender
                         ,Place=place,
                         Username=username
                         ,Password=password
                         ,DOB=dob
                         ,Mobile=mobile)
    customer.save()
    messages.add_message(request,messages.INFO,"registration was successful")
    return render(request, "index.html")
    
    
def customerview(request):
    product=product_tb.objects.all()
    return render(request,"customerview.html",{'view':product})


def addtocart(request,id):
    product=product_tb.objects.filter(id=id)
    return render(request,"cart.html",{'view':product}) 


def cartaction(request):
    productid=request.POST['id']  
    customer_id= request.session["customerid"]
    shippingaddress=request.POST['address']
    phone=request.POST['mobile']
    quantity=request.POST['quanty']
    total=request.POST['total']
    stock=request.POST['stock'] 
    if int(stock)<int(quantity):
         messages.add_message(request,messages.INFO,"invalid quantity")
         return redirect(customerview)
    else:
        user=cart_tb(productid_id=productid,
                        customer_id_id=customer_id,
                        shipping_address=shippingaddress,
                        phone=phone,
                        quantity=quantity,
                        total=total)
        user.save()
    messages.add_message(request,messages.INFO,"item added to cart ")
    return redirect(customerview) 


def viewcart(request):
    grandtotal=0
    customer_id=request.session['customerid']
    cart=cart_tb.objects.filter(customer_id_id=customer_id)
    for i in cart:
        total=i.total
        grandtotal=grandtotal+total
    if len(cart)<0:
         messages.add_message(request,messages.INFO,"cart is empty")
    else:
        return render(request,"viewcart.html",{'view':cart,"gtotal":grandtotal})
    
    
def deleteitem(request,id):
    customer_id=request.session['customerid']
    grandtotal=0
    cart=cart_tb.objects.filter(id=id).delete()
    carts=cart_tb.objects.filter(customer_id_id=customer_id)
    for i in carts:
        total=i.total
        grandtotal=grandtotal+total
    if len(cart)<0:
         messages.add_message(request,messages.INFO,"cart is empty")
    else:
        return render(request,"viewcart.html",{'view':carts,"gtotal":grandtotal})
    
    
def orderaction(request):
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    customer_id=request.session['customerid']
    grandtotal=request.POST['grandtotal']
    orderdate=datetime.date.today()
    ordertime=datetime.datetime.now().strftime("%H:%M")

    order=order_table(name=name,
                     address=address,
                     customer_id_id=customer_id,
                     phone=phone,
                     order_date=orderdate,
                     order_time=ordertime,
                     grandtotal=grandtotal)
    order.save()

    cart=cart_tb.objects.filter(customer_id_id=customer_id)
    for i in cart:
        cartitem=cart_tb.objects.filter(id=i.id)
        productid=cartitem[0].productid.id 
        quantity=cartitem[0].quantity
        stock=cartitem[0].productid.stock
        total=cartitem[0].total
        newstock=stock-quantity
        product_tb.objects.filter(id=productid).update(stock=newstock)
        orderitem=oderitems_table(quantity=quantity,
                                  total=total,
                                  customer_id_id=customer_id,
                                  order_id_id=order.id,
                                  productid_id=productid

                                  
                                  )
        orderitem.save()
    messages.add_message(request,messages.INFO,"please choose the payment option")
    return redirect ("payment",order.id)
    
def payment(request,id):
     id=order_table.objects.filter(id=id)     
     return render(request,"payment.html",{'views':id})
 
def paymentaction(request):    
    cardname=request.POST['cardname']
    cardnumber=request.POST['cardnumber']
    cvv=request.POST['cvv']
    expdate=request.POST['expdate']
    customer_id=request.session['customerid']
    orderid=request.POST['orderid']
    
    pay=payment_tb(cardname=cardname,
                      cardnumber=cardnumber,
                      cvv=cvv,
                      expiary_date=expdate,
                      customer_id_id=customer_id,
                      orderid_id=orderid)
    
    pay.save()
    messages.add_message(request,messages.INFO,"payment  successfull")
    return render(request,"customer_home.html")


def viewdetails(request):
    customer_id=request.session['customerid']
    details=order_table.objects.filter(customer_id_id=customer_id)
    return render(request,"viewdetails.html",{'view':details}) 



def details(request,id):
    orderdetails=order_table.objects.filter(id=id)
    customer_id=request.session['customerid']
    orderid=oderitems_table.objects.filter(order_id_id=id,customer_id_id=customer_id)
    return render(request,"orderdetails.html",{'view':orderdetails,'views':orderid})

def cancelorder(request,id):
     order_table.objects.filter(id=id).update(status="canceled")
     return redirect('viewcart')