
from django.urls import path

from equipamentos import views


app_name = 'equipamentos'

urlpatterns = [    
    path('', views.equipamentos, name='equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('deletar/<slug:slug>/', views.remover_equipamento, name='remover_equipamento'),
    path('editar/<slug:slug>/', views.editar_equipamento, name='editar_equipamento'),
    path('visualizar/<slug:slug>/', views.visualizar_equipamento, name='visualizar_equipamento'),
    path('comentario/status/<pk>/', views.comment_status, name='comment-status'),
    path('comentario/adicionar/<pk>/', views.comment_sent, name='comment-sent'),
    path('comentario/editar/<pk>/', views.comment_edit, name='comment-edit'),
    path('comentario/deletar/<pk>/', views.comment_delete_view, name='comment-delete'),
    path('resposta/status/<pk>/', views.reply_status, name='reply-status'),
    path('resposta/adicionar/<pk>/', views.reply_sent, name='reply-sent'),
    path('resposta/editar/<pk>/', views.reply_edit, name='reply-edit'),
    path('resposta/deletar/<pk>/', views.reply_delete_view, name='reply-delete'),
    path('marcar/lido/<slug:slug>', views.marcar_notificacao_lida, name='marcar_notificacao_lida'),
    
    path('autocomplete/', views.autocomplete, name='autocomplete'),
]