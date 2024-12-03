from unicodedata import category

from django.shortcuts import render
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
    form = SignupForm

    return render(request, 'marketPlace/signup.html', {
        'form': form
    })