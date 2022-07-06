
"""procube URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from core.views import  authentication as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',auth.login),
    path('login',auth.login_process),
    

]
