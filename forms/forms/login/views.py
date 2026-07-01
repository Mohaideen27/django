from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def manual_form_view(request):
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('useremail')

        if not name or not email:
            return HttpResponse("Error: All fields are required.")
        
        return HttpResponse(f'Success! Received user:{name}')
    
    return render(request, 'manual_form.html')

def home(request):
    return HttpResponse("Welcome home")