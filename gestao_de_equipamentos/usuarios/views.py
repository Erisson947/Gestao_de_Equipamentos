from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse

from usuarios import models

from django.contrib.auth.models import Group



def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('laboratorios:laboratorios'))
    contexto = {
        'title': 'Login',
    }
    return render(
        request,
        'usuarios/pages/login.html',
        contexto
    )


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect(reverse('usuarios:login'))


def perfil(request):
    context = {'title': f'Perfil - { request.user.name }'}
    # REMOVE LATER
    reg = models.User.objects.first()
    reg.is_admin = True
    reg.is_staff = True
    reg.is_superuser = True
    reg.save()
    # REMOVE LATER
    return render(
        request,
        'usuarios/pages/perfil.html',
        context
    )
