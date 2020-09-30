from django.shortcuts import render
import json 
# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def family(request, family_id):
    with open('info/animals.json') as f:
        data = json.load(f)
    families = data["families"]
    fam = None
    for family in families:
        if family_id == family["id"]:
            fam = family
    animals = None
    if fam:
        animals = [animal for animal in data["animals"] if animal["family"] == fam["id"]]
    

    return render(request, 'family.html', {"animals": animals, "fam": fam})
    
def animal(request):
    return render(request, 'animal.html')

