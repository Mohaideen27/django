from django.urls import path
from . import views
urlpatterns=[
    path("", views.quickWithdraw),
    path("customWithdraw/", views.customWithdraw),
    path("withdrawSuccess/", views.withdrawSuccess, name='withdrawSuccess')
]