from django.db import models

class UsuarioModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

class TarefaModel(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField()
    data_conclusao = models.DateTimeField()
    id_usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)

#Renomeando a Tabela
class Meta:
    db_table = 'agenda'
    
    def __str__(self):
        return self.titulo