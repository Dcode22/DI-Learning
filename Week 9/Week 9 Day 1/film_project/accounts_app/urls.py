from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns= [
    path('profile/', views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage.html'), name="logout"),
    path('signup/', views.signup, name="signup")
]