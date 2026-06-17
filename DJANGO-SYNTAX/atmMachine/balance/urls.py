from django.urls import path
from . import views

urlpatterns = [
    path('',views.checkBalance),
    path('miniStatment/',views.miniStatement),
]
