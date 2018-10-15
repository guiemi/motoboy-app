from django.shortcuts import render
from .forms import EmpresaForm, MotoboyForm
from solicitacao.models import Empresa, Solicitacao
from django.http import HttpResponseRedirect, HttpResponse


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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = EmpresaForm()

    context = {"form": form}
    return render(request, 'cadastro_empresa.html', context)


def solicitacao_motoboy(request):
    if request.method == 'POST':
        form = MotoboyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = MotoboyForm()

    context = {"form": form}
    return render(request, 'solicitacao_motoboy.html', context)


def detalhes_solicitacao(request, pk):
    return HttpResponse(f'Teste de PK: {pk}')
