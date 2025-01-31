from django.urls import path

from laboratorios import views

app_name = 'laboratorios'

urlpatterns = [
 
    path('', views.laboratorios, name='laboratorios'),
    path('lista/', views.laboratorio_list, name='laboratorio_list'),
    path('adicionar/', views.adicionar_laboratorio, name='adicionar_laboratorio'),
    path('<slug:slug>/horario/adicionar/', views.adicionar_horario, name='adicionar_horario'),
    path('<slug:slug>/professor/adicionar/', views.adicionar_professor, name='adicionar_professor'),
    path('<slug:slug>/projeto/adicionar/', views.adicionar_projeto, name='adicionar_projeto'),
    path('<slug:slug>/servico/adicionar/', views.adicionar_servico, name='adicionar_servico'),
    path('<slug:slug>/equipamento/adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('<slug:slug>/material/adicionar/', views.adicionar_material, name='adicionar_material'),
    path('<slug:slug>/foto/adicionar/', views.adicionar_foto, name='adicionar_foto'),
    path('<slug:slug>/visualizar/', views.visualizar_laboratorio, name='visualizar_laboratorio'),
    path('<slug:slug>/editar/', views.editar_laboratorio, name='editar_laboratorio'),
    path('<slug:slug>/deletar/', views.remover_laboratorio, name='remover_laboratorio'),
]