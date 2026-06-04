"""
URL configuration for views project.

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
from views import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home),
    path("student/<str:id>/",views.students),
    path("details/<str:name>/<str:place>/<str:course>/",views.details),
    # path("student1/", views.student1),
    # path("student2/", views.student2),
    # path("student3/", views.student3),
    # path("student4/", views.student4),
    # path("student5/", views.student5),
    # path("student6/", views.student6),
    # path("student7/", views.student7),
    # path("student8/", views.student8),
    # path("student9/", views.student9),
    # path("student0/", views.student0),
]
