from django.urls import path, include
from . import views


urlpatterns = [
   path('animals/', views.animals, name='info-animals'),
   path('animal/<int:id>', views.animal, name='animal'),
   path('family/<int:id>', views.family, name='family')
]
