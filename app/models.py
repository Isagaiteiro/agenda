from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField()
    data_conclusao = models.DateTimeField()
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

