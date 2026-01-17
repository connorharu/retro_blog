from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Jogos, Acessorios
from .forms import FormularioJogos, FormularioAcessorios

# Create your views here.

# def index(request):
#     return HttpResponse("começo da página dos objetos")

def cadastro_jogos(request):
    if request.method == "POST":
        form = FormularioJogos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormularioJogos()
    
    return render(request, 'registrar_jogos.html', {'form': form})

def cadastro_acessorios(request):
    if request.method == "POST":
        form = FormularioAcessorios(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormularioAcessorios()
    
    return render(request, 'registrar_acessorios.html', {'form': form})