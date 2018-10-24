from django.shortcuts import render, redirect
from .forms import EmpresaForm, MotoboyForm
from solicitacao.models import Empresa, Solicitacao
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Páginas principais


@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def index(request):
    cadastros = Empresa.objects.all()
    solicitacoes = Solicitacao.objects.all()

    return render(request, 'index.html', {
        'cadastros': cadastros,
        'solicitacoes': solicitacoes,
        'user': request.user.username,
    })


@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def cadastro_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = EmpresaForm()

    context = {"form": form, "cadastro_active": "active"}
    return render(request, 'cadastro_empresa.html', context)


@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def solicitacao_motoboy(request):
    if request.method == 'POST':
        form = MotoboyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = MotoboyForm()

    context = {"form": form, "solicitacao_active": "active"}
    return render(request, 'solicitacao_motoboy.html', context)


def sobre(request):
    context = {"sobre_active": "active"}
    return render(request, 'sobre.html', context)

# Páginas secundárias:


@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def detalhes_solicitacao(request, pk):
    detalhes = Solicitacao.objects.get(pk=pk)

    return render(request, 'detalhes_solicitacao.html', {
        'detalhes': detalhes,
    })


# Editar:
@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def editar_empresa(request, pk):
    empresa = Empresa.objects.get(pk=pk)

    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = EmpresaForm(instance=empresa)

    context = {'form': form}
    return render(request, 'cadastro_empresa.html', context)


@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def editar_solicitacao(request, pk):
    solicitacao = Solicitacao.objects.get(pk=pk)

    if request.method == "POST":
        form = MotoboyForm(request.POST, instance=solicitacao)
        if form.is_valid:
            form.save()
        return redirect(f"/detalhes_solicitacao/{solicitacao.pk}")
    elif request.method == "GET":
        form = MotoboyForm(instance=solicitacao)

    context = {'form': form}
    return render(request, 'solicitacao_motoboy.html', context)


# Deletar:
@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def deletar_cadastro(request, pk):
    cadastro = Empresa.objects.get(pk=pk)
    cadastro.delete()
    return HttpResponseRedirect("/")


@login_required(login_url='login')  # Redir. p/ login usuário deslogado
def deletar_solicitacao(request, pk):
    cadastro = Solicitacao.objects.get(pk=pk)
    cadastro.delete()
    return HttpResponseRedirect("/")
