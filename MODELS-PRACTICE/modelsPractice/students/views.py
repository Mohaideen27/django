from django.shortcuts import render
from .models import studentDetails
# Create your views here.

def createStudent(request):
    studentDetails.objects.create(
        name='sameer',
        rNo=4048,
        course='MERN STACK',
    )
    return render(request,'success.html')

def allStudents(request):
    students=studentDetails.objects.all()
    context={
        students:students
    }
    return render(request,'oneStudent.html',context)

def updateStudent(request):
    student=studentDetails.objects.get(id=1)
    student.rNo=210
    student.save()
    return render(request,'success.html')

def deleteStudent(request):
    student=studentDetails.objects.get(id=1)
    student.delete()
    return render(request, 'success.html')

def dashboard(request):
    sc=studentDetails.objects.count()
    students=studentDetails.objects.all()
    context={
        'studentCount':sc,
        'students':students,
    }
    return render(request,'dashboard.html',context)