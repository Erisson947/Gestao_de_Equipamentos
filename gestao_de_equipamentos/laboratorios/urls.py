from django.urls import path

from laboratorios import views

app_name = 'laboratorios'

urlpatterns = [
 
    path('', views.laboratorios, name='laboratorios'),
    path('lista/', views.laboratorio_list, name='laboratorio_list'),
    path('adicionar/', views.add_laboratorio, name='add_laboratorio'),
    path('<slug:slug>/equipamentos/', views.view_equipamentos_laboratorio, name='view_equipamentos_laboratorio'),
    path('<slug:slug>/editar/', views.edit_laboratorio, name='edit_laboratorio'),
    path('<slug:slug>/deletar/', views.remove_laboratorio, name='remove_laboratorio'),
    path('marcar/lido/', views.marcar_notificacao_laboratorio_lida, name='marcar_notificacao_laboratorio_lida'),
]