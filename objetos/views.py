from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Jogos, Acessorios
from .forms import FormularioJogos, FormularioAcessorios
from django.db import models

# Create your views here.

# def index(request):
#     return HttpResponse("começo da página dos objetos")

def cadastro_jogos(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = FormularioJogos(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormularioJogos()
    
    return render(request, 'registrar_jogos.html', {'form': form})

def cadastro_acessorios(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = FormularioAcessorios(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormularioAcessorios()
    
    return render(request, 'registrar_acessorios.html', {'form': form})

def get_jogos(console):
    if console == 'SFC':
        return Jogos.objects.filter(console='SFC')
    if console == 'WII':
        return Jogos.objects.filter(console='WII')
    if console == 'PS2':
        return Jogos.objects.filter(console='PS2')
    if console == '3DS':
        return Jogos.objects.filter(console='3DS')

def get_acessorios(console):
    if console == 'SFC':
        return Acessorios.objects.filter(console='SFC')
    if console == 'WII':
        return Acessorios.objects.filter(console='WII')
    if console == 'PS2':
        return Acessorios.objects.filter(console='PS2')
    if console == '3DS':
        return Acessorios.objects.filter(console='3DS')