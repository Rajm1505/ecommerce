from email import message
from django.shortcuts import render, redirect
    
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .models import Products

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


def viewCart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')
