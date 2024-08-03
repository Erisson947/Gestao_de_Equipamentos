from django.urls import path

from notificacoes import views

app_name = 'notificacoes'

urlpatterns = [
 
    path('', views.notificacoes, name='notificacoes'),
    path('categoria/<categoria>/', views.notificacoes, name='categoria_notif'),
    path('marcar/lido/todos/', views.marcar_notificacoes_lidas, name='marcar_todas_notificacoes_lidas'),
    path('marcar/lido/<categoria>/', views.marcar_notificacoes_lidas, name='marcar_notificacoes_lidas'),
    path('marcar/lido/<slug:slug>/', views.mark_as_read, name='mark_as_read'),
]