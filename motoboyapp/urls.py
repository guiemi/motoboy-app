from django.contrib import admin
from django.urls import path, include
from solicitacao import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
# from django.views.generic.base import TemplateView

app_name = 'solicitacao'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cadastro_empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('solicitacao_motoboy/', views.solicitacao_motoboy, name='solicitacao_motoboy'),
    path('detalhes_solicitacao/<int:pk>', views.detalhes_solicitacao, name='detalhes_solicitacao'),
    path('sobre/', views.sobre, name='sobre'),
    path('editar_empresa/<int:pk>', views.editar_empresa),
    path('deletar_cadastro/<int:pk>', views.deletar_cadastro, name='deletar_cadastro'),
    path('deletar_solicitacao/<int:pk>', views.deletar_solicitacao, name='deletar_solicitacao'),
    path('editar_solicitacao/<int:pk>', views.editar_solicitacao, name='editar_solicitacao'),
]
