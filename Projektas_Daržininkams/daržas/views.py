from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def naujas(request):
    return HttpResponse("Sveiki")