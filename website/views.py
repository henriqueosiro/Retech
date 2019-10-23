from django.shortcuts import render, redirect
from website.models import *

def cadastro(request):
    if request.method == 'POST':
        data_usuario = Cadastro()
        data_usuario.descricao = request.POST['descricao']
        data_usuario.email = request.POST['email']
        data_usuario.foto = request.POST['foto']
        data_usuario.nascimento = request.POST['nascimento']
        data_usuario.nome = request.POST['nome']
        data_usuario.novidades = request.POST['novidades']
        data_usuario.regiao = request.POST['regiao']
        data_usuario.senha = request.POST['senha']
        data_usuario.sexo = request.POST['sexo']
        data_usuario.telefone = request.POST['telefone']

        args = {
            'resposta': 'Parabéns, você conseguiu fazer uma doação. Muito obrigado!'
        }

        return render(request, 'cadastro.html', args)

    return render(request, 'index.html')


