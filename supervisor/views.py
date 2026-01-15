from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Supervisor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
import re

# Create your views here.

def cadastro_supervisor(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # senha = form.cleaned_data.get('password1')
            # supervisor = authenticate(username=username, password=senha)
            # login(request, supervisor)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registrar.html', {'form': form})