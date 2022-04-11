from django.shortcuts import render
from django.HttpResponse import httpresponse



def home():
    return HttpResponse("Hello Django")

# Create your views here.
