from django.urls import path
from . import views

urlpatterns=[
    path("",views.mobile),
    path("redmi/",views.redmi),
    path("oppo/",views.oppo),
    path("vivo/",views.vivo),
]