from django import forms
from django.forms import ModelForm
from rent.models import *
import datetime

class Addrental(forms.Form):
    rental_date=forms.DateField(required= False)
    return_date=forms.DateField(required= False)
    customer=forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle=forms.ModelChoiceField(queryset=Vehicle.objects.all())

# class Addrental(ModelForm):
#      class Meta:
#          model = Rental
#          fields = '__all__'