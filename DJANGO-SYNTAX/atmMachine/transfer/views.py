from django.shortcuts import render

# Create your views here.
def transfer(request):
    return render(request, './transfer/transfer.html')

def transferVerification(request):
    return render(request, './transfer/transferVerification.html')

def transferSuccess(request):
    return render(request, './transfer/transferSuccess.html')