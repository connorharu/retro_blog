from django.urls import path
from . import views

urlpatterns = [
    path("jogos/", views.cadastro_jogos, name="registrar_jogos"),
    path("acessorios/", views.cadastro_acessorios, name="registrar_acessorios"),
]