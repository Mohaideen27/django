from django.http import HttpResponse
from django.http import HttpResponseNotFound

def home(request):
    return HttpResponse("<h1> Hi soldiers</h1>")

def students(request,id):
    html={"Mohaideen":["python","Tenkasi"],"Naveen":["python","Ramanadhapuram"],"Dinesh":["Java","Thiruporur"],"Kathir":["Web tech","Thanjavur"]}
    if id in html.keys():
        return HttpResponse(f"My name is {id} and i am from {html[id][1]}. I am pursuing {html[id][0]} in qspiders")
    else:
        return HttpResponseNotFound
def details(request,name,place,course):
    return HttpResponse(f"My name is {name} and i am from {place}. I am pursuing {course} in qspiders")

# def student1(request):
#     student="Mohaideen"
#     return HttpResponse(student)

# def student2(request):
#     student="Sameer"
#     return HttpResponse(student)

# def student3(request):
#     student="Naveen"
#     return HttpResponse(student)

# def student4(request):
#     student="dinesh"
#     return HttpResponse(student)

# def student5(request):
#     student="harish"
#     return HttpResponse(student)

# def student6(request):
#     student="kathir"
#     return HttpResponse(student)

# def student7(request):
#     student="nandha"
#     return HttpResponse(student)

# def student8(request):
#     student="vasanth"
#     return HttpResponse(student)

# def student9(request):
#     student="nithish"
#     return HttpResponse(student)

# def student0(request):
#     student="sivaraj"
#     return HttpResponse(student)