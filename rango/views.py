from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    str1 = "Rango says hey there partner!"+ "</p>" + "<a href='/rango/about/'>About</a>"
    return HttpResponse(str1)

def about(request):
    str2 = "Rango says here is the about page." + "</p>" + "<a href='/rango/'>Index</a>"
    return HttpResponse(str2)
