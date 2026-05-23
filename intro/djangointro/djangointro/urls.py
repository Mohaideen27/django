"""
URL configuration for djangointro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def homepage(req):
    return render(req,'index.html')
def allpage(req):
    return render(req)
def freshpage(req):
    return render(req)
def sellpage(req):
    return render(req)
def bestsellerspage(req):
    return render(req)
def mobilespage(req):
    return render(req)
def todaysDealpage(req):
    return render(req)
def newReleasepage(req):
    return render(req)
def customerServicePage(req):
    return render(req)
def premiumPage(req):
    return render(req)
def walletPage(req):
    return render(req)

def aboutpage(req):
    return render('<h1>Welcome to the about page</h1>')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage),
    # path("all/", allpage),
    # path("fresh/", freshpage),
    # path("sell/", sellpage),
    # path("bestsellers/", bestsellerspage),
    # path("mobiles/", mobilespage),
    # path("todays-deals/", todaysDealpage),
    # path("new-release/", newReleasepage),
    # path("customer-service/", customerServicePage),
    # path("premium/", premiumPage),
    # path("wallet/", walletPage),
    # path("about/", aboutpage),
]
