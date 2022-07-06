from django.shortcuts import render

def login(request):
    return render(request,'registration/login.html')

def login_process(request):
    if request.method =! 'POST':
        pass
    else:
        pass
