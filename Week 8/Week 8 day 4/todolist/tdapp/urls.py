from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name= "home"),
    path('signup/', views.signup , name= "signup"),
    path('login/', views.login , name= "login"),
    path('addtodo/', views.addtodo , name= "addtodo"),
    path('viewtodo/<int:id>', views.viewtodo , name= "viewtodo")
]
