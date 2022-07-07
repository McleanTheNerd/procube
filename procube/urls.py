
"""procube URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from core.views import  authentication as auth
from django.conf.urls.static import static

from procube import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("core.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
