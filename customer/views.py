from email import message
from django.shortcuts import render, redirect,HttpResponse
    
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .models import Products, Cart, User

from django.forms.utils import ErrorDict


# Create your views here.
def index(request):
    products = Products.objects.all()
    ranges = range(0,len(products))
    context = {'products' : products, 'noofproducts' : range(1,len(products)+1) }

    return render(request, 'customer/home.html', context=context)

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
            
       
    return render(request, 'customer/login.html')

def logoutView(request):
    logout(request)
    return redirect( '/login')


def register(request):
    
    form = UserForm()
    context={}
    context['form'] = form
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('/login')
        else:
            context['form'] = form 
            print(form.errors)
            # print("type1",type(str(form.errors)))
            # print("type1",type(ErrorDict(form.errors)))
            # context['formerrors']=form.errors
            # for i in form.errors:
            #     print("element: ",i)
            # errors = str(form.errors['email']).replace("<li","<li class='list-group-item")
            # print("email: ",errors)
            # context['formerrors'] = 
            # messages.error(request,str(form.errors))
            return render(request, 'customer/register.html',context=context)
            # return redirect('/register')
        
        
    return render(request, 'customer/register.html', context=context)

def productDetails(request):
    id = request.GET.get('id')
    try:
        product = Products.objects.get(pid=id)
        context = {'product': product}
    except:
        context = {'error': "Product does not exist"}


    return render(request,'customer/productdetails.html',context=context)

def productsPage(request):
    query = str(request.POST.get('searchquery')).strip()
    print("query:",query)
    if query is None or query =='':
        return redirect('/')
    
    products = Products.objects.filter(name__icontains= query)
    if not products:
        messages.error(request,"No Products found 404")
    print("products",products)
    context = {'products': products,'query':query}
    return render(request,'customer/productspage.html',context=context)


def viewCart(request):
    uid =  User.objects.get(uid = request.user.uid) 
    cart = Cart.objects.filter(uid=uid)
    if not cart:
        messages.error(request,"No Products found")
    print(cart)
    context = {'cart' : cart}
    
    return render(request, 'customer/cart.html' ,context=context)


def addToCart(request):
    id = request.GET.get('id')
    pid = Products.objects.get(pid = id)
    uid =  User.objects.get(uid = request.user.uid) 
    source = request.GET.get('source')
    print(source)
    try:
        cart = Cart.objects.get(pid = pid,uid=uid)
        messages.success(request,"Product is already in the cart")
    except:
        cart = Cart(uid = uid,pid=pid)
        cart.save()
        messages.success(request,"Successfully added to cart")
    if source is not None:
        return redirect(f'/productdetails?id={id}')
    else: 
        return redirect('/')


def removeFromCart(request):
    id = request.GET.get('id')
    try:
        cart = Cart.objects.get(pid = id,uid = request.user.uid)
        cart.delete()
    except:
        pass
    return redirect('/viewcart')

def contact(request):
    return render(request, 'customer/contact.html')

def test(request):
    return render(request, 'customer/testproductpage.html')
