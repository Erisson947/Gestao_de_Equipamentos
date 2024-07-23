from django.urls import path

from tags import views

app_name = 'tags'

urlpatterns = [
 
    path('', views.tags, name='tags'),
    path('list/', views.tags_list, name='tags_list'),
    path('criar/', views.tag_create, name='tag_create'),
    path('<slug:slug>/equipamentos/', views.view_equipamentos_tag, name='view_equipamentos_tag'),
    path('editar/<slug:slug>/', views.tag_edit, name='tag_edit'),
    path('deletar/<slug:slug>/', views.tag_delete, name='tag_delete'),
    path('marcar/lido/', views.marcar_notificacao_tag_lida, name='marcar_notificacao_tag_lida'),
]