# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# def home(request):
#     return HttpResponse("I am home page")

def details(request):
    return HttpResponse("<h1> Hi I am Mohaideen </h1>")

def home(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())