from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
    cep = models.CharField(min_length=8, max_length=8, verbose_name='CEP')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    nome = models.CharField(max_length=255, verbose_name='Nome')
    regiao = 
    telefone = models.IntegerField(min_length=11, max_length=11, verbose_name='Telefone')
    senha = models.CharField(min_length=8, max_length=16, verbose_name='Senha')

class Doacao(models.Model):
    criado_em = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição do Equipamento')
    equipamento = models.CharField(max_length=255, verbose_name='Nome do Equipamento')
    foto = models.ImageField(verbose_name='Foto do Equipamento')
