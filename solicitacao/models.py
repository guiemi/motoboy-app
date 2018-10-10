from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=25)


class Solicitacao(models.Model):
    data = models.DateField()
    solicitante = models.CharField(max_length=30)
    endereco_origem = models.CharField(max_length=50)
    contato_origem = models.CharField(max_length=30)
    servico = models.TextField()
    endereco_destino = models.CharField(max_length=30)
    contato_destino = models.CharField(max_length=30)
    observacoes = models.TextField()
