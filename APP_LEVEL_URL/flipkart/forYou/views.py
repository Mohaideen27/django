from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse

def homePage(request):
    return HttpResponse("homepage")

def login(request):
    return HttpResponse("Login page")

def cart(request):
    return HttpResponse("Cart page")

def deals(request):
    return HttpResponse("deals page")