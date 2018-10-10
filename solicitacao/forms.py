from django import forms  # from django.forms import ModelForm
from .models import Empresa, Solicitacao
from django.utils.translation import gettext_lazy as _


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        # fields = '__all__'
        fields = ('nome', 'cnpj')
        labels = {
            'nome': _('Nome'),
            'cnpj': _('CNPJ'),
        }


class MotoboyForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'
        #  Campos: data, solicitante, endereco_origem, contato_origem,
        # servico, endereco_destino, contato_destino, observacoes
        labels = {
            'endereco_origem': _('Endereço de origem'),
            'contato_origem': _('Contato de origem'),
            'servico': _('Serviço'),
            'endereco_destino': _('Endereço de destino'),
            'contato_destino': _('Contato de destino'),
            'observacoes': _('Observações'),
        }
