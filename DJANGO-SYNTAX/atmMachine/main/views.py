from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcomePage(request):
    return render(request,'index.html')

def selectLanguage(request):
    return render(request,"./main/languages.html")

def enterPin(request):
    return render(request,"./main/enterPin.html")

def services(request):
    return render(request, './main/services.html')

def exit(request):
    return render(request, './main/exitPage.html')