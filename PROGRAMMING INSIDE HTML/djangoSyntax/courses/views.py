from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def course_list(request):
    courses = {"Python for Beginners" : ["Learn Python from scratch.", "/python"] , "Django Web Development" : ["Build web applications with Django.", "/django"] , "Data Science with Python" : ["Analyze data using Python.","/data-science"]}
    context={'courses': courses}
    return render(request, "nav.html",context)

def python(request):
    return HttpResponse("Python page")

def Django(request):
    return HttpResponse("Django page")

def DataScience(request):
    return HttpResponse("DataScience page")