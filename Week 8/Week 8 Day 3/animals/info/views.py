from django.shortcuts import render
from .models import Animal, Family

# Create your views here.
def animals(request):
    animals = Animal.objects.all()
    context = {
        "animals": animals
    }

    html = render(request, 'animals.html', context)

    return html

def family(request, id):
    family = Family.objects.get(id=id)
    familyanimals = Animal.objects.filter(family=id)
    
    html = render(request, 'family.html', {"familyanimals": familyanimals, "family": family})
    return html 

def animal(request, id):
    animal = Animal.objects.get(id=id)
    html = render(request, 'animal.html', {"animal":animal})
    return html 