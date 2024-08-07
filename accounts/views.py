from django.shortcuts import render,redirect
from truda.models import Truda_truth,Truda_dare
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.http import JsonResponse

import random

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            elif username =="":
                messages.info(request, 'Fill in the boxes')
                return redirect('register')
            elif email =="":
                messages.info(request, 'Fill in the boxes')
                return redirect('register')
            elif password1 =="":
                messages.info(request, 'Fill in the boxes')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Account created')
                return redirect('home')
        else:
            messages.info(request, 'password does not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')


def signup(request):
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def getruth(request):
    truth = Truda_truth.objects.all()
    return JsonResponse({'truth': random.choice(list(truth.values()))})

def getdare(request):
    dare = Truda_dare.objects.all()
    return JsonResponse({'dare': random.choice(list(dare.values()))})