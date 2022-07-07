from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from db.models import CustomUser

from core.EmailBackEnd import EmailBackEnd

def register(request):
    return render(request, 'registration/signup.html')

def registration(request):
    if request.method != "POST":
        messages.error(request, 'method used not allowed')
        return redirect('register')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=3)
            user.save()
            messages.success(request, "account created successfully!")
            return HttpResponseRedirect('login_index')
        except:
            messages.error(request, "registration failed , contact help desk")
            return redirect('register')



def loginPage(request):
    return render(request, 'registration/login.html')



def login_process(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            auth_login(request,user)
            messages.success(request, "Welcome , "+user.username)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "invalid login credentials!")
            return HttpResponseRedirect('/')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("please login first")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
