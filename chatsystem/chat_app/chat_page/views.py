from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def printname(request) : 
    return render(request, "stranger.html")
