from django.http import HttpResponse, HttpResponseNotFound
import datetime
from django.shortcuts import render
def home(request):
    return HttpResponse("this is home page")
def tour(request):
    now=datetime.datetime.now()
    html='<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
def calls(request):
    # Get the 'status' value from the URL query string (e.g., ?status=missing)
    status_param = request.GET.get('stats', '')
    
    # Simple logic: if the user passes status=missing, trigger the 404
    if status_param == 'notfound':
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")
def party(request):
    return HttpResponse(status=201)
def food(request):
    return HttpResponseNotFound("<h1>Page not found</h1>")
def bikes(request):
    return render(request, "bikes.html")
