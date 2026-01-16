from django.db import models

# Create your models here.

class Jogos(models.Model):
    CONSOLES_CHOICES = [
        ('SFC', 'Super Famicom'),
        ('WII', 'Nintendo Wii'),
        ('PS2', 'Playstation 2'),
        ('3DS', 'Nintendo 3DS')
    ]

    TIPO_CHOICES = [
        ('CAR', 'Cartucho'),
        ('DIS', 'Disco'),
        ('DIG', 'Digital')
    ]
    
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    console = models.CharField(max_length=3, choices=CONSOLES_CHOICES)
    nome = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    ano = models.IntegerField(default=0)
    genero = models.CharField(max_length=30) # to-do: verificar generos e fazer listagem
    descricao = models.CharField(max_length=1000)

class Acessorios(models.Model):
    nome = models.CharField(max_length=30)
    ano = models.IntegerField(default=0)
    descricao = models.CharField(max_length=1000)  