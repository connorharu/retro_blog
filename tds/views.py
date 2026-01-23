from django.shortcuts import render
from django.http import HttpResponse
from objetos.views import get_acessorios, get_jogos

# Create your views here.

def tds_main(request):
    jogos = get_jogos('3DS')
    acessorios = get_acessorios('3DS')
    return render(request, '3ds_main.html', {'jogos':jogos, 'acessorios':acessorios})