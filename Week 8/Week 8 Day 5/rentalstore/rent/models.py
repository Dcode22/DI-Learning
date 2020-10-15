from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=40)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)


class Vehicle_type(models.Model):
    name=models.CharField(max_length=30)


class Vehicle_size(models.Model):
    name=models.CharField(max_length=30)

class Vehicle(models.Model):
    vehicle_type=models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    date_created=models.DateField()
    real_cost=models.IntegerField()
    size=models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)

class Rental(models.Model):
    rental_date=models.DateField(auto_now_add= True)
    return_date=models.DateField(null= True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class Rental_rate(models.Model):
    daily_rate=models.IntegerField()
    vehicle_type=models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    vehicle_size=models.ForeignKey(Vehicle_size, on_delete=models.CASCADE)

 
