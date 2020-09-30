from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    context = {
        "name":"DOVID"
    }
    return render(request, 'home.html', context=context)