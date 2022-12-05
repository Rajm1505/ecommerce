from email import message
from django.shortcuts import render, redirect,HttpResponse
    
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .models import Products, Cart, User


# Create your views here.
def index(request):
    products = Products.objects.all()
    context = {'products' : products}
    return render(request, 'home.html', context=context)

def loginView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,email = email, password = password)

        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.info(request, "Username or Password is incorrect!")
            print('hello')
            
       
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect( '/login')


def register(request):
    
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('/login')
        else:
            print(form.errors)
            return redirect('/register')
        
        
    context = {'form':form}
    
    return render(request, 'register.html', context=context)

def productDetails(request):
    id = request.GET.get('id')
    product = Products.objects.get(pid=id)
    context = {'product': product}

    return render(request,'productdetails.html',context=context)

def productsPage(request):
    query = str(request.POST.get('searchquery')).strip()
    print("query:",query)
    if query is None or query =='':
        return redirect('/')
    
    products = Products.objects.filter(name__icontains= query)
    print("products",products)
    context = {'products': products,'query':query}
    return render(request,'productspage.html',context=context)


def viewCart(request):
    uid =  User.objects.get(uid = request.user.uid) 
    cart = Cart.objects.filter(uid=uid)
    print(cart)
    context = {'cart' : cart}
    
    return render(request, 'cart.html' ,context=context)


def addToCart(request):
    id = request.GET.get('id')
    pid = Products.objects.get(pid = id)
    uid =  User.objects.get(uid = request.user.uid) 
    try:
        cart = Cart.objects.get(pid = pid,uid=uid)
    except:
        cart = Cart(uid = uid,pid=pid)
        cart.save()
    return redirect(f'/productdetails?id={id}')

def removeFromCart(request):
    id = request.GET.get('id')
    try:
        cart = Cart.objects.get(pid = id,uid = request.user.uid)
        cart.delete()
    except:
        pass
    return redirect('/viewcart')

def contact(request):
    return render(request, 'contact.html')
