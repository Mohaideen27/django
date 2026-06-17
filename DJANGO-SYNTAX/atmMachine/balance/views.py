from django.shortcuts import render

# Create your views here.
def checkBalance(request):
    return render(request, './balance/checkBalance.html')

def miniStatement(request):
    return render(request, './balance/miniStatement.html')
