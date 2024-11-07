from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.TextField(max_length=11)
    telefone = models.TextField(max_length=14)
    idade = models.DateField()
    senha = models.CharField(max_length=20)

class Agendamento(models.Model):
    id_agendamento= models.AutoField(primary_key=True)
    nome_agendamento = models.TextField(max_length=255, blank=True)
    especialidade_agendamento = models.TextField(max_length=255, blank=True)  
    medico_agendamento = models.TextField(max_length=255, blank=True)
    data_agendamento = models.DateField(blank=True)  
    hora_agendamento = models.TimeField(blank=True)

    
