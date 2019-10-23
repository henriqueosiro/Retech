from django.db import models
from django.utils import timezone

class Cadastro(models.Model):

    NOVIDADES = (
        ('s', 'Sim'),
        ('n', 'Não'),
    )

    REGIAO = (
        ('p.1', 'Zona Norte'),
        ('p.2', 'Zona Sul'),
        ('p.3', 'Zona Leste'),
        ('p.4', 'Zona Oeste'),
    )
    SEXO = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
        ('n', 'None'),
    )   

    criado_em = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição do Equipamento')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    foto = models.ImageField(verbose_name='Foto do Equipamento')
    nascimento = models.DateField(verbose_name='Data de Nascimento')
    nome = models.CharField(max_length=255, verbose_name='Nome')
    novidades = models.CharField(choices=NOVIDADES, verbose_name='Novidades')
    regiao = models.CharField(choices=REGIAO, verbose_name='Região')
    senha = models.CharField(min_length=8, max_length=16, verbose_name='Senha')
    sexo = models.CharField(choices=SEXO, verbose_name='Sexo')
    telefone = models.IntegerField(min_length=11, max_length=11, verbose_name='Telefone')

class Contato(models.Model):
    assunto = models.CharField(max_length=255, verbose_name='Assunto')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    mensagem = models.TextField(verbose_name='Mensagem')
    nome = models.CharField(max_length=255, verbose_name='Nome')