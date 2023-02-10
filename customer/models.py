from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null = True)
    refreshtoken = models.CharField(max_length=255, default=None,null=True)
    otp = models.SmallIntegerField(null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.uid)


# class Userdetails(models.Model):

#     uid = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)

#     address = models.CharField(max_length=255, default = None )


#     def __str__(self):
#         return self.name






category_choices = (
    ("accessories","Accessories"),
    ("clothing","Clothing"),
    ("healthcare","Healthcare"),
)
class Products(models.Model):
    pid = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 255, default = None)
    description = models.CharField(max_length = 255, default = None)
    category = models.CharField(max_length = 255, default = None, choices = category_choices)
    price = models.IntegerField(default = None)
    rating = models.IntegerField(default = None)
    image1 = models.ImageField(upload_to="static/images/products",default = None)
    image2 = models.ImageField(upload_to="static/images/products",default = None)



   

    def __str__(self):
        return self.name


class Cart(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE)
    

    

    def __str__(self):
        return self.uid.name

   

  
