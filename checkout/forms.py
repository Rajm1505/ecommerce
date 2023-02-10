from django.forms import ModelForm
from .models import Useraddress

class UseraddressForm(ModelForm):
    class Meta:
        model = Useraddress
        fields = '__all__'
    

