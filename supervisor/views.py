from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Supervisor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
# import re

# Create your views here.

def cadastro_supervisor(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registrar.html', {'form': form})

def login_supervisor(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_supervisor(request):
    logout(request)
    return redirect('index')