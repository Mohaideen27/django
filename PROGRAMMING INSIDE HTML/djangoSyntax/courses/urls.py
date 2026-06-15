from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list),
    path("python/", views.python),
    path("django/", views.Django),
    path("data-science/", views.DataScience)
]