from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcomePage(request):
    return render(request,'index.html')

def selectLanguage(request):
    return render(request,"languages.html")
    # return HttpResponse("select language")

def enterPin(request):
    # return HttpResponse("enter pin")
    return render(request,"enterPin.html")

def services(request):
    return HttpResponse("Service Page")