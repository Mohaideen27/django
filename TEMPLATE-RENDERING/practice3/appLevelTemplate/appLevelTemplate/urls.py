from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls')),
    path("chennai/",include('app1.urls')),
    path("bangalore/",include('app2.urls')),
    path("other-place/",include('app3.urls')),
]
