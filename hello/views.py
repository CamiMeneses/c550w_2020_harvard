from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def camila(request):
    return HttpResponse("Hello, Camila!")

def new_year(request):
    return HttpResponse("Happy New Year")

def greet_v(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render (request, "hello/greet.html", {
      "name": name.capitalize()
    })
