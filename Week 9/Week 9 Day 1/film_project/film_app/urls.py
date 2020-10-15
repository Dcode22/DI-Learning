from django.urls import path
from . import views

urlpatterns= [
    path('home/', views.homepage, name="homepage"),
    path('adddirector/', views.AddDirector.as_view(), name="addDirector"),
    path('addfilm/', views.AddFilm.as_view(), name="addFilm"),
    path('delete/<str:title>', views.deletefilm, name="delete")
]