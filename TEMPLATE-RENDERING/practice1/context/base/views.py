from django.shortcuts import render

# Create your views here.
def about(request, name, age,place):
    context={'name':name,"age":age,"place":place}
    return render(request, 'index.html', context)