from django.db import models
from customer.models import User

# Create your models here.
addresstypechoices = (
    ('home','Home'),
    ('work','Work')
)

class Useraddress(models.Model):
    aid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150,default = None)
    phone = models.CharField(max_length=10,default=None)
    pincode = models.CharField(max_length=6,default=None)
    locality = models.CharField(max_length=100,default=None,null=True)
    address = models.CharField(max_length=255, default = None )
    city = models.CharField(max_length=50,default=None)
    state = models.CharField(max_length=50,default=None)
    addresstype = models.CharField(max_length = 30,choices=addresstypechoices)


    def __str__(self):
        return str(self.aid)

class Orders(models.Model):
    oid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    pids = models.CharField(max_length=200,default=None)
    aid = models.ForeignKey(Useraddress,on_delete=models.CASCADE,default = None)
    price = models.IntegerField()
    deliverycharges = models.IntegerField(null=True)
    orderdate = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.oid)

   
