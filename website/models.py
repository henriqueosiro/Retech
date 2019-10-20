from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    nome = models.CharField(max_length=255, verbose_name='Nome')
    senha = models.CharField(max_length=16, verbose_name='Senha')

class Doacao(models.Model):
    cep = models.CharField(min_length=8, max_length=8, verbose_name='CEP')
    criado_em =  models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    equipamento = models.CharField(max_length=255, verbose_name='Equipamento')
