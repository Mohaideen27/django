from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
def add(request,a,b):
    res=a+b
    return HttpResponse(res)
# def home(request):
#     return render(request, 'index.html')
# def home(request):
#     return render(request, 'index.html')