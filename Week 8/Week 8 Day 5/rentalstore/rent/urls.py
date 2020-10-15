from django.urls import path
from . import views 
urlpatterns = [
    path('home/', views.home, name= "home"),
    path('rental', views.allrentals, name= "rental"),
    path('rental/<int:id>', views.viewrental, name= "rentalid"),
    path('rental/add', views.addrental, name= "rentaladd"),
    # path('customer', views.allcustomers, name= "customer"),
    # path('customer/<pk>', views.viewcustomer, name= "customerid"),
    # path('customer/add', views.addcustomer, name= "customeradd"),
    # path('vehicle', views.allvehicles, name= "vehicle"),
    # path('vehicle/<pk>', views.viewvehicle, name= "vehicleid"),
    # path('vehicle/add', views.addvehicle, name= "vehicleadd"),
]