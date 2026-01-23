from django.shortcuts import render
from django.http import HttpResponse
from objetos.views import get_jogos, get_acessorios

# Create your views here.

def index(request):
    return render(request, 'pagina_principal.html')

def sfc_main(request):
    jogos = get_jogos('SFC')
    acessorios = get_acessorios('SFC')
    return render(request, 'sfc_main.html', {'jogos':jogos, 'acessorios':acessorios})