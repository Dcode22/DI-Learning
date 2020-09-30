from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.homepage),
    path('family/<int:family_id>', views.family)
]