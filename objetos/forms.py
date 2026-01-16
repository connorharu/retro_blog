
from django import forms
from .models import Jogos

class FormularioJogos(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ['nome', 'tipo', 'console', 'publisher', 'ano', 'genero', 'descricao']