from django.urls import path
from . import views

urlpatterns = [
    path('', views.transfer),
    path('transferVerification/', views.transferVerification),
    path('transferSuccess/',views.transferSuccess, name='transferSuccess')
]
