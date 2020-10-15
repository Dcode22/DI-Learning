from django import forms
from django.forms import ModelForm
from film_app.models import *
import datetime

class AddFilmForm(forms.ModelForm):
    class Meta:
        model= Film
        fields= '__all__'
        widgets = {
            'title': forms.TextInput(attrs= {"placeholder": "Enter Movie Title", "class": "form-control"}),
            # 'release_date'= models.DateField(auto_now_add= True)
            # 'created_in_country':  models.ForeignKey(Country, on_delete=models.CASCADE, related_name= 'created_films')
            # available_in_countries= models.ManyToManyField(Country, related_name='available_films')
            'category': forms.CheckboxSelectMultiple()
            # director= models.ManyToManyField(Director)
        }

class AddDirectorForm(forms.ModelForm):
    class Meta: 
        model= Director
        fields= '__all__'