from django.contrib import admin
from django.urls import path, include
from adminapp import views as views2
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('adminapp.urls')),
    path('', include('staffhub.urls')),
    path('', include('clienthub.urls')),
    path('', lambda request: redirect('staffhub:home')),
]
