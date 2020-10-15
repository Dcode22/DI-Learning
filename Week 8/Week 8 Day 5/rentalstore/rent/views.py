from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Customer, Vehicle, Vehicle_size, Vehicle_type, Rental, Rental_rate

# Create your views here.
def home(request):
    return render(request, 'home.html')


def allrentals(request):
    content = Rental.objects.all()
    return render(request, 'rentals.html', {"content": content })


def viewrental(request, id):
    rental = Rental.objects.get(id=id)
    return render(request, 'rental.html', {"rental": rental })


def addrental(request):
    
    
    if request.method == 'GET':
        form = Addrental()
        return render(request, "addrental.html", {'form': form})

    if request.method == 'POST':
        form = Addrental(request.POST)
        if form.is_valid():

            Rental.objects.create(
                rental_date = form.cleaned_data['rental_date'],
                return_date = form.cleaned_data['return_date'],
                customer = form.cleaned_data['customer'],
                vehicle = form.cleaned_data['vehicle']
            )
        else:
            return print('not valid form')
    
    return render(request, 'addrental.html')

    
# def allcustomers(request):
# def viewcustomer(request):
# def addcustomer(request):
# def allvehicles(request):
# def viewvehicle(request):
# def addvehicle(request):






 
 
 


