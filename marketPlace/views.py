from unicodedata import category

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from item.models import Category, Item
# from django.http import HttpResponse
from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'marketPlace/index.html', {
        'categories':categories,
        'items':items,
    })

def contact(requst):
    return render(requst, 'marketPlace/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('marketPlace:index')
        else:
            return render(request, 'marketPlace/signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'marketPlace/signup.html', {'form': form})