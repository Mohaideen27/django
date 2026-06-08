from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mobile(request):
    return HttpResponse("mobile home page")

def redmi(request):
    return HttpResponse("redmi mobile homepage")

def oppo(request):
    return HttpResponse("oppo mobile homepage")

def vivo(request):
    return HttpResponse("vivo mobile homepage")