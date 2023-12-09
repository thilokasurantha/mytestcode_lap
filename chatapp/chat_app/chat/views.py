from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.
def printname(request) :
    return HttpResponse("Thiloka Surantha is my name")


