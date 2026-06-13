from urllib import request

import courses

from django.shortcuts import render

# Create your views here.
def course_list(request):
    # courses =[
    #     {"name": "Python for Beginners", "description": "Learn Python from scratch."},
    #     {"name": "Django Web Development", "description": "Build web applications with Django."},
    #     {"name": "Data Science with Python", "description": "Analyze data using Python."},
    # ]

    courses = {"Python for Beginners" : "Learn Python from scratch." , "Django Web Development" : "Build web applications with Django." , "Data Science with Python" : "Analyze data using Python."}
    context={'courses': courses}
    return render(request, "index.html")