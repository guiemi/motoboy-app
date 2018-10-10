from django.shortcuts import render
from .forms import EmpresaForm, MotoboyForm
from solicitacao.models import Empresa, Solicitacao


def index(request):
    cadastros = Empresa.objects.all()
    solicitacoes = Solicitacao.objects.all()

    return render(request, 'index.html', {
        'cadastros': cadastros,
        'solicitacoes': solicitacoes,
    })




def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        form.save()
    else:
        form = EmpresaForm()

    context = {"form": form}
    return render(request, 'cadastro_empresa.html', context)


def solicitacao_motoboy(request):
    if request.method == 'POST':
        form = MotoboyForm(request.POST)
        form.save()
    else:
        form = MotoboyForm()

    context = {"form": form}
    return render(request, 'solicitacao_motoboy.html', context)
