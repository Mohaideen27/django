from django.urls import path
from . import views

urlpatterns = [
    path("",views.depositCredential),
    path("verification/",views.verification),
    path("depositSuccess/", views.depositSuccess, name='depositSuccess')
]
