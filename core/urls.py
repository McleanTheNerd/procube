
"""procube URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from .views import  authentication as auth
from django.conf.urls.static import static

from procube import settings

urlpatterns = [
    path('',auth.loginPage),
    path('login_process',auth.login_process),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
