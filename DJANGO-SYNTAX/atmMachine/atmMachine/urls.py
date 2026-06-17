from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('main.urls')),
    path("withdraw/", include('withdraw.urls')),
    path("deposit/",include('deposit.urls')),
    path("transfer/",include('transfer.urls')),
    path('balance/',include('balance.urls')),
    path('pinChange/',include('pinChange.urls')),
]
