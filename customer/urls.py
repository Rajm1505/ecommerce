"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
import checkout

urlpatterns = [
   
    path('', views.index, name = "home"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('register', views.register, name="register"),
    path('productdetails', views.productDetails, name="productdetails"),
    path('productspage', views.productsPage, name="productspage"),
    path('viewcart', views.viewCart, name="viewcart"),
    path('addtocart', views.addToCart, name="addtocart"),
    path('removefromcart', views.removeFromCart, name="removefromcart"),
    path('test', views.test, name="test"),
    path('checkout/', include('checkout.urls'),name="checkout"),
]
