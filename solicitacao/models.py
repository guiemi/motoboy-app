from django.db import models
from datetime import date


class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=25, unique=True)
    '''O 'unique=True' impede CNPJs duplicados
    '''

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete="CASCADE", related_name='empresa_id')

    data = models.DateField(default=date.today)
    solicitante = models.CharField(max_length=30)
    endereco_origem = models.CharField(max_length=50)
    contato_origem = models.CharField(max_length=30)
    servico = models.TextField()
    endereco_destino = models.CharField(max_length=30)
    contato_destino = models.CharField(max_length=30)
    observacoes = models.TextField()


