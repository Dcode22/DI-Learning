from faker import Faker 
import random
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rentalstore.settings')
django.setup()
from rent.models import *
fake= Faker()
if Customer.objects.all().count() < 20:

    for i in range(10):
        first_name = fake.first_name() 
        last_name = fake.last_name()
        customer = Customer.objects.create(
            first_name= first_name,
            last_name= last_name,
            email= f"{first_name}.{last_name}@example.com",
            phone_number= fake.phone_number() ,
            address= fake.street_address(),
            city= fake.city(),
            country= fake.country(),

        )

# vehicle_types = [
#     "scooter",
#     "motorcycle",
#     "bike",
#     "jetpack"
# ]

# for name in vehicle_types:
#     Vehicle_type.objects.get_or_create(name= name)

# vehicle_sizes = [
#     "small",
#     "medium",
#     "large"
# ]

# for size in vehicle_sizes:
#     Vehicle_size.objects.get_or_create(name= size)

while Vehicle.objects.count() < 20:
    Vehicle.objects.create(
        vehicle_type= random.choice(Vehicle_type.objects.all()),
        date_created= fake.date_between(start_date='-1y', end_date='today'),
        real_cost= random.randint(30, 200),
        size= random.choice(Vehicle_size.objects.all())
    )

for vehicle_type in Vehicle_type.objects.all():
    for vehicle_size in Vehicle_size.objects.all():
        rental_rate, created = Rental_rate.objects.get_or_create(vehicle_type= vehicle_type, vehicle_size= vehicle_size)
        if created:
            rental_rate.daily_rate= random.randint(10, 200)