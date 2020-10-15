from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, YearArchiveView
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    user = request.user 
 
    films= Film.objects.all()
    return render(request, 'homepage.html', {'films': films})


class AddFilm(CreateView):
    model= Film
    form_class= AddFilmForm 
    template_name= 'film/addfilm.html'
    
    success_url= reverse_lazy('homepage')


class AddDirector(CreateView):
    model= Director
    form_class= AddDirectorForm 
    template_name= 'film/adddirector.html'
    success_url= reverse_lazy('homepage')
    

def deletefilm(request, title):
    Film.objects.filter(title=title).delete()
    messages.success(request, 'Film Successfully Deleted!')
    return redirect('homepage')

       

from django.contrib import messages

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was updated successfully!')  # <-
            return redirect('settings:password')
        else:
            messages.warning(request, 'Please correct the error below.')  # <-
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profiles/change_password.html', {'form': form})


