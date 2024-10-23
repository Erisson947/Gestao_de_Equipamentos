from django.urls import path

from laboratorios import views

app_name = 'laboratorios'

urlpatterns = [
 
    path('', views.laboratorios, name='laboratorios'),
    path('lista/', views.laboratorio_list, name='laboratorio_list'),
    path('adicionar/', views.add_laboratorio, name='add_laboratorio'),
    path('<slug:slug>/horario/adicionar/', views.add_horario, name='add_horario'),
    path('<slug:slug>/visualizar/', views.visualizar_laboratorio, name='visualizar_laboratorio'),
    path('<slug:slug>/editar/', views.edit_laboratorio, name='edit_laboratorio'),
    path('<slug:slug>/deletar/', views.remove_laboratorio, name='remove_laboratorio'),
    path('marcar/lido/', views.marcar_notificacao_laboratorio_lida, name='marcar_notificacao_laboratorio_lida'),
]