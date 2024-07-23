from django.shortcuts import redirect
from django.urls import reverse, path

from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('accounts/profile/', lambda request: redirect(reverse('equipamentos:equipamentos'))),
    path('', lambda request: redirect(reverse('equipamentos:equipamentos'))),
]