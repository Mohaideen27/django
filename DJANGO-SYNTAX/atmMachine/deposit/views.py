from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def depositCredential(request):
    return render(request, './deposit/credential.html')

def verification(request):
    return render(request, './deposit/verification.html')

def depositSuccess(request):
    return render(request, './deposit/depositSuccess.html')