from django.shortcuts import render
from .forms import EmpresaForm, MotoboyForm


def index(request):
    return render(request, 'index.html', {})


def cadastro_empresa(request):
    form = EmpresaForm()
    context = {"form": form}
    return render(request, 'cadastro_empresa.html', context)


def solicitacao_motoboy(request):
    form = MotoboyForm
    context = {"form": form}
    return render(request, 'solicitacao_motoboy.html', context)
