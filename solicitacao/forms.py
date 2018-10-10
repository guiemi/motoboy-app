from django import forms
from .models import Empresa, Solicitacao


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class MotoboyForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'
