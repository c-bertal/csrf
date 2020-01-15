"""csrf URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('csrf/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
