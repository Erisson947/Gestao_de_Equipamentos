from django.urls import path

from pegar_chave import views

app_name = 'pegar_chave'

urlpatterns = [
    path('', views.chaves, name='chaves'),
    path('<estilo>/', views.chaves, name='estilo_chaves'),
    path('chave/adicionar/', views.adicionar_chave, name='adicionar_chave'),
    path('chave/editar/<slug:slug>/', views.editar_chave, name='editar_chave'),
    path('chave/deletar/<slug:slug>/', views.deletar_chave, name='deletar_chave'),
    path('pegar/<chave_slug>/', views.pegar_chave, name='pegar_chave'),
    path('pegar/confirmar/<chave_slug>/<matricula_usuario>/', views.pegar_chave, name='confirmar_pegar_chave'),
    path('pegada/<slug:slug>/', views.visualizar_chave_pegada, name='visualizar_chave_pegada'),
    path('pegada/devolver/<slug:slug>/', views.devolver_chave_pegada, name='devolver_chave_pegada'),
    path('pegada/deletar/<slug:slug>/', views.deletar_chave_pegada, name='deletar_chave_pegada'),
]