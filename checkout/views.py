from django.shortcuts import render, HttpResponse, redirect
from .forms import UseraddressForm
from .models import Useraddress, Orders
from customer.models import User,Cart, Products
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.
@api_view(('GET','POST'))
def address(request):
    addressform = UseraddressForm()
    uid = User.objects.get(uid = request.user.uid)
    addresses = Useraddress.objects.filter(uid = uid )
    context = {
        "form":addressform,
        "addresses" : addresses
    }
    
    if request.method == 'GET':
        # API to get address from aid as input 
        if request.GET.get('aid') is not None:
            address = Useraddress.objects.get(aid=request.GET.get('aid'))
            response =Response()
            response.data = {
                "address" : address

            }
            return response
        source = request.GET.get('source')
        context['source'] = source
        # if request comes from cart
        if source == 'cart':
            cart = Cart.objects.filter(uid=request.user.uid) 
            
            context['totalprice'] = totalPrice(cart)
            context['cart'] = cart
                
            return render(request,'checkout/address.html',context=context)
            
        # if request comes from productdetails page
        elif source == 'productdetails':
            product = Products.objects.get(pid=request.GET.get('id')) 
            context['product'] = product
            


            return render(request,'checkout/address.html',context=context)
        return render(request,'checkout/address.html',context=context)

    
        
        
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['uid'] = uid
        print("requestpost",request.POST)
        addressform = UseraddressForm(request.POST)
        # addressform.data['uid'] = uid
        if addressform.is_valid():
            print("cleaned:",addressform.cleaned_data)
            addressform.save()
            messages.success(request,"Address added successfully")
            return redirect('/checkout/address')
        else:
            print(addressform.errors)
            messages.error(request,str(addressform.errors))
            return redirect('/checkout/address')

def totalPrice(cart):
    price = 0
    for product in cart:
        price += product.pid.price
    return price


@api_view(('GET',))
def placeOrder(request):
    aid = Useraddress.objects.get(aid=request.GET.get("aid")) 
    source = request.GET.get('source')
    user = User.objects.get(uid = request.user.uid)
    request.session['address'] = aid.aid
    request.session['source'] = source

    if source == "cart":
        cart = Cart.objects.filter(uid = user)
        products = []
        for product in cart:
            products.append(product.pid.pid)

        order = Orders()
        order.uid = user
        order.pids = str(products)
        order.aid = aid
        order.price = totalPrice(cart)
        order.deliverycharges = 0 if order.price > 499 else 50
        order.save()
        cart.delete()
        


        print("products: ",products)
        request.session['orderid'] = order.oid

        print("cart: ",cart)
        return redirect("invoice")
        
    
    elif source == "productdetails":
        product = Products.objects.get(pid = request.GET.get('pid'))
        order = Orders()
        order.uid = user
        orderlist = [product.pid,]
        order.pids = str(orderlist)
        order.aid = aid
        order.price = product.price
        order.deliverycharges = 0 if order.price > 499 else 50
        order.save()
        messages.success(request,f"Order has been successfull placed! Use Orderid: {order.oid} to track your order.")

        request.session["productid"] = product.pid

        return redirect('invoice')

def invoice(request):
    try:
        oid = request.GET.get("oid")
        order = Orders.objects.get(oid = oid)
        products = order.pids
    except:
        pass
    return render(request,'checkout/invoice.html')

def payment(request):
    return HttpResponse("this is payment page")
            