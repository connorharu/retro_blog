from django.shortcuts import render
from django.http import HttpResponse
from objetos.views import get_jogos, get_acessorios

# Create your views here.

def ps2_main(request):
    jogos = get_jogos('PS2')
    acessorios = get_acessorios('PS2')
    return render(request, 'ps2_main.html', {'jogos':jogos, 'acessorios':acessorios})