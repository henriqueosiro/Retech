from django.db import models
from django.utils import timezone

class Cadastro(models.Model):

    NOVIDADES = (
        ('s', 'Sim'),
        ('n', 'Não'),
    )

    REGIAO = (
        ('p.0', 'Centro'),
        ('p.1', 'Zona Leste'),
        ('p.2', 'Zona Norte'),
        ('p.3', 'Zona Oeste'),
        ('p.4', 'Zona Sul'),
    )
    SEXO = (
        ('f', 'Feminino'),
        ('m', 'Masculino'),
        ('n', 'None'),
    )   
    criado_em = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(verbose_name='Descrição do Equipamento')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    foto = models.ImageField(verbose_name='Foto do Equipamento')
    nascimento = models.DateField(verbose_name='Data de Nascimento')
    nome = models.CharField(max_length=255, verbose_name='Nome')
    novidades = models.CharField(max_length=3, choices=NOVIDADES, verbose_name='Novidades')
    regiao = models.CharField(max_length=10, choices=REGIAO, verbose_name='Região')
    senha = models.CharField(max_length=16, verbose_name='Senha')
    sexo = models.CharField(max_length=9, choices=SEXO, verbose_name='Sexo')
    telefone = models.IntegerField(max_length=11, verbose_name='Telefone')

    def __str__(self):
        return self.nome

class Contato(models.Model):
    assunto = models.CharField(max_length=255, verbose_name='Assunto')
    criado_em = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    mensagem = models.TextField(verbose_name='Mensagem')
    nome = models.CharField(max_length=255, verbose_name='Nome')

    def __str__(self):
        return self.nome