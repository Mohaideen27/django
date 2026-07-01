from django.urls import path
from . import views
urlpatterns = [
    path("",views.manual_form_view),
    path("home/",views.home)
]
