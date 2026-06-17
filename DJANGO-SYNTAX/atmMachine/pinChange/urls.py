from django.urls import path
from . import views

urlpatterns = [
    path('',views.pinChange),
    path('pinChangeSuccess/',views.pinChangeSuccess),
]
