from django.shortcuts import redirect, render 
from django.http import HttpResponse
from .models import Agendamento, Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def auth(request):
    return render(request, 'usuarios/auth.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome_usuario')
    novo_usuario.email = request.POST.get('email_usuario')
    novo_usuario.cpf = request.POST.get('cpf_usuario')
    novo_usuario.telefone = request.POST.get('telefone_usuario')
    novo_usuario.idade = request.POST.get('idade_usuario')
    novo_usuario.senha = request.POST.get('senha_usuario')
    novo_usuario.save()

    # Exibir todos os usuarios cadastrados em uma nova página
    usuarios = {
        'usuarios':  Usuario.objects.all()
    }
    
    # Retornar os dados para a página de listagem
    return render(request,'usuarios/usuarios.html',usuarios)

def agendamentos(request):
    # Salvar os dados da tela para o banco de dados
    novo_agendamento = Agendamento()
    novo_agendamento.nome_agendamento = request.POST.get('nome_agendamento')
    novo_agendamento.especialidade_agendamento = request.POST.get('especialidade_agendamento')
    novo_agendamento.medico_agendamento = request.POST.get('medico_agendamento')
    novo_agendamento.data_agendamento = request.POST.get('data_agendamento')
    novo_agendamento.hora_agendamento = request.POST.get('hora_agendamento')
    novo_agendamento.save()

    # Exibir todos os agendamentos cadastrados em uma nova página
    agendamentos = {
        'agendamentos':  Agendamento.objects.all()
    }
    
    # Retornar os dados para a página de listagem
    return render(request,'usuarios/marcados.html',agendamentos)
        
def marcados(request):
    return render(request, 'usuarios/agendamento.html')