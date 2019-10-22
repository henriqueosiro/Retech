from django.db import models
from django.utils import timezone

class Cadastro(models.Model):
    criado_em = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição do Equipamento')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    equipamento = models.CharField(max_length=255, verbose_name='Nome do Equipamento')
    foto = models.ImageField(verbose_name='Foto do Equipamento')
    nascimento = models.DateField(verbose_name='Data de Nascimento')
    nome = models.CharField(max_length=255, verbose_name='Nome')
    senha = models.CharField(min_length=8, max_length=16, verbose_name='Senha')
    telefone = models.IntegerField(min_length=11, max_length=11, verbose_name='Telefone')

class Contato(models.Model):
    assunto = models.CharField(max_length=255, verbose_name='Assunto')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    mensagem = models.TextField(verbose_name='Mensagem')
    nome = models.CharField(max_length=255, verbose_name='Nome')