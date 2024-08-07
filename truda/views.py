from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'main.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('home')
    else:
        return render(request, 'home.html')