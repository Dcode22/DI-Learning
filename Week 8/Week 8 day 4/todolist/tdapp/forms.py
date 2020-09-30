from django import forms
import datetime

class Signupform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Loginform(forms.Form):
    username = forms.CharField(max_length= 30)
    password = forms.CharField(widget=forms.PasswordInput)

class Addtodoform(forms.Form):
    user= forms.IntegerField()
    title= forms.CharField(max_length= 30)
    details= forms.CharField(max_length= 100)
    has_been_done= forms.BooleanField(initial= False, required= False)
    date_creation= forms.DateField(initial= datetime.date.today)
    date_completion= forms.DateField(required= False)
    deadline_date= forms.DateField()
