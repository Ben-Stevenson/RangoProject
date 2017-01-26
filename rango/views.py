from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href ="/rango/about"> button </a>')

#def about(request):
    return HttpResponse('<a href ="/rango/about"> button </a>')