from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def marketPlaceView(request):
    return HttpResponse("This is a test!")