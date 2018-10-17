"""motoboyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from solicitacao import views

app_name = 'solicitacao'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastro_empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('solicitacao_motoboy/', views.solicitacao_motoboy, name='solicitacao_motoboy'),
    path('detalhes_solicitacao/<int:pk>', views.detalhes_solicitacao, name='detalhes_solicitacao'),
    path('sobre/', views.sobre, name='sobre'),
    path('editar_empresa/<int:pk>', views.editar_empresa),
    path('deletar_cadastro/<int:pk>', views.deletar_cadastro, name='deletar_cadastro'),
    path('editar_solicitacao/<int:pk>', views.editar_solicitacao, name='editar_solicitacao'),
]
