from django.shortcuts import render,redirect
from shop.models import shop_tb
from customer.models import customer_tb
from shop.models import product_tb
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")


def login(requet):
    return render(requet, "login.html") 

def loginaction(request):
    username=request.POST['username']
    password=request.POST['password']
    customer_username=request.POST['username']
    customer_password=request.POST['password']
    shop=shop_tb.objects.filter(Username=username,Password=password)
    customer=customer_tb.objects.filter(Username=customer_username,Password=customer_password)
    if (shop.count()>0):
        request.session['shopid']=shop[0].id
        return render(request, 'shop.html')
    elif (customer.count()>0):
        request.session['customerid']=customer[0].id
        return render(request, "customer_home.html")
    else:
        return render(request, 'login.html')
    
 
def customer_view(request):
    customer=customer_tb.objects.all()
    return render(request, "view_customer.html", {'view':customer})    


def addproduct(request):
    return render(request, "addproduct.html")


def addproductaction(request):
    name = request.POST["name"]
    price = request.POST['price']
    details = request.POST['details']
    stock = request.POST['stock']
    shop_id = request.session['shopid']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img="no pic"

    product = product_tb(
        name=name,
        price=price,
        details=details,
        stock=stock,
        shop_id_id=shop_id,
        image=img
    )
    product.save()
    messages.add_message(request,messages.INFO,"product added successfully")
    return redirect("addproduct") 


def viewproduct(request):
    product=product_tb.objects.all()
    return render(request, "viewproduct.html",{'view':product}) 


def edit_product(request,id):
    product=product_tb.objects.filter(id=id)
    return render(request, "editproduct.html", {'view':product})


def editproduct_action(request):
    id=request.POST['id']
    product=product_tb.objects.filter(id=id)
    name = request.POST["name"]
    price = request.POST['price']
    details = request.POST['details']
    stock = request.POST['stock']
    shop_id = request.session['shopid']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img=product[0].image
    pr=product_tb.objects.get(id=id)
    pr.image=img
    pr.save()
    product_tb.objects.filter(id=id).update(
        name=name,
        price=price,
        details=details,
        stock=stock,
        shop_id_id=shop_id,
    )
    messages.add_message(request,messages.INFO,"product updated successfully")
    return redirect("viewproduct")


def delete_product(request,id):
    product_tb.objects.filter(id=id).delete()
    return redirect("viewproduct")


