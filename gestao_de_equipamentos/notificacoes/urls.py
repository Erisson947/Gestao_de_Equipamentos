from django.urls import path

from notificacoes import views

app_name = 'notificacoes'

urlpatterns = [
 
    path('', views.notificacoes, name='notificacoes'),
    path('marcar/lido/equips/', views.marcar_notificacoes_lidas_equips, name='marcar_notificacoes_lidas_equips'),
    path('marcar/lido/labs/', views.marcar_notificacoes_lidas_labs, name='marcar_notificacoes_lidas_labs'),
    path('marcar/lido/tags/', views.marcar_notificacoes_lidas_tags, name='marcar_notificacoes_lidas_tags'),
    path('marcar/lido/todos/', views.marcar_todas_notificacoes_lidas, name='marcar_todas_notificacoes_lidas'),
    path('marcar/lido/<slug:slug>/', views.mark_as_read, name='mark_as_read'),
]