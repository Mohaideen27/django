from django.shortcuts import render

# Create your views here.
def pinChange(request):
    return render(request,'./pinChange/pinChange.html')

def pinChangeSuccess(request):
    return render(request,'./pinChange/pinChangeSuccess.html')