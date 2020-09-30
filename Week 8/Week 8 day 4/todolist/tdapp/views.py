from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Signupform, Loginform, Addtodoform
from .models import User, Todo

# Create your views here.

def base(request):
    return render(request, "base.html")

def signup(request):
    if request.method == 'GET':
        form = Signupform()
        return render(request, 'signup.html', {'form' : form})


    if request.method == 'POST':
        form = Signupform(request.POST)

        if form.is_valid():

            user = User.objects.create(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            # return redirect('login')

    return render(request, "signup.html")

def login(request):
     if request.method == 'GET':
        form = Loginform()
        return render(request, 'login.html', {'form' : form})


    # if request.method == 'POST':
    #     form = Loginform(request.POST)

    #     if form.is_valid():

    #         user = User.objects.create(
    #             username=form.cleaned_data['username'], 
    #             password=form.cleaned_data['password']
    #         )
    #         return redirect('todo/')

    #  return redirect('todo/' form.username )
    
def addtodo(request):
     if request.method == 'GET':
        form= Addtodoform()
        return render(request, "addtodo.html", {'form': form})
    
     if request.method == 'POST':
         form = Addtodoform(request.POST)

         if form.is_valid():

             todo = Todo.objects.create(
                 user=form.cleaned_data['user'], 
                 title=form.cleaned_data['title'],
                 details=form.cleaned_data['details'],
                 has_been_done=form.cleaned_data['has_been_done'],
                 date_creation= form.cleaned_data['date_creation'],
                 date_completion= form.cleaned_data['date_completion'],
                 deadline_date= form.cleaned_data['deadline_date']
             )
            # return redirect('login')

def viewtodo(request, id):
    todo = Todo.objects.get(id=id)
    html = render(request, 'viewtodo.html', {"todo": todo})
    return html
