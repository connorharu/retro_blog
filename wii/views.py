from django.shortcuts import render
from django.http import HttpResponse
from objetos.views import get_jogos, get_acessorios

# Create your views here.

def wii_main(request):
    jogos = get_jogos('WII')
    acessorios = get_acessorios('WII')
    return render(request, 'wii_main.html', {'jogos':jogos, 'acessorios':acessorios})