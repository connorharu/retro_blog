from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField

    def __str__(self):
        return f"Supervisor: {self.user.nome}"