from django.urls import path
from . import views

urlspatterns=[
    path('',views.homePage),
    path('login/',views.login),
    path('cart/',views.cart),
    path('deals/',views.deals),
]