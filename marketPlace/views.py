from unicodedata import category

from django.shortcuts import render, redirect
from item.models import Category, Item
from django.http import HttpResponseNotAllowed
from .forms import SignupForm
from django.contrib.auth import logout

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
        form= SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm

    return render(request, 'marketPlace/signup.html', {
        'form': form
    })

def about(request):
    return render(request, 'marketPlace/about.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)  # Log out the user
        return redirect('marketPlace:login')  # Redirect to login page
    else:
        return HttpResponseNotAllowed(['POST'])  # Return 405 if method is not POST