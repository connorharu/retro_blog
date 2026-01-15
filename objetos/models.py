from django.db import models

# Create your models here.

class Cartuchos(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    ano = models.IntegerField(default=0)
    genero = models.CharField(max_length=30)

class Acessorios(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=30)
    ano = models.IntegerField(default=0)   