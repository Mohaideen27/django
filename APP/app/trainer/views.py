from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trainer(request):
    return HttpResponse("trainer template")