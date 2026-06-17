from django.urls import path
from . import views

urlpatterns = [
    path("",views.welcomePage),
    path("language/",views.selectLanguage),
    path("pin/",views.enterPin),
    path("services/",views.services)
]
