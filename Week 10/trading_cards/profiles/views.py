from django.contrib.auth import login, authenticate
from .models import Profile, Card, Sale
from .forms import SignUpForm, EditProfileForm, EditUserForm
from django.shortcuts import render, redirect
import random


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile= Profile.objects.create(user=user)
            cards= random.sample(list(Card.objects.all()), k=10)
            profile.cards_owned.add(*cards)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):

    sales = request.user.profile.sales.all()
    cards_for_sale = [] 
    for sale in sales:
        cards_for_sale.append(sale.card)

    offers = request.user.profile.bids.all()
    cards_offered= []
    for offer in offers:
        cards_offered.append(offer.card)

    content = {
        "cards_for_sale": cards_for_sale, 
        "cards_offered": cards_offered
        }

    return render(request, 'profile.html', content)


def editProfile(request):
    if request.method == 'POST':
        form1 = EditProfileForm(data=request.POST, instance=request.user.profile)
        form2 = EditUserForm(data=request.POST, instance=request.user)
        form1.save()
        form2.save()
        # update.user = request.user
        return redirect('profile')
    else:
        form1 = EditProfileForm(instance=request.user.profile)
        form2 = EditUserForm(instance=request.user)


    return render(request, 'edit_profile.html', {'form1': form1, 'form2': form2})