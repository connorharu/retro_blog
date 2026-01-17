
from django import forms
from .models import Jogos, Acessorios

class FormularioJogos(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ['nome', 'tipo', 'console', 'publisher', 'ano', 'genero', 'descricao']

class FormularioAcessorios(forms.ModelForm):
    class Meta:
        model = Acessorios
        fields = ['nome', 'ano', 'console', 'descricao']