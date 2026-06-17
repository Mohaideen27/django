from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def quickWithdraw(request):
    return render(request, "./withdraw/quickWithdraw.html")

def customWithdraw(request):
    return render(request, './withdraw/customWithdraw.html')

def withdrawSuccess(request):
    return render(request, './withdraw/transactionSuccessful.html')
