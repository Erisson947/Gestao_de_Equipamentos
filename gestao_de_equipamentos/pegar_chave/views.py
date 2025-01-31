from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
import json
from pegar_chave import forms, models, tasks
from django.contrib import messages
from django.db.models import ProtectedError
from django.db import IntegrityError
from usuarios.models import User
from .tasks import checar_chaves_atrasadas
from django.core.mail import send_mail
    
def chaves(request, estilo=False):
    chaves = models.Chave.objects.filter(campus=request.user.campus).order_by('bloco_num')
    chaves_pegadas = models.Pegar_Chave.objects.filter(chave__campus=request.user.campus)
    
    send_mail(
        'Ola mundo!',
        'todo mundo está bem',
        'no-reply@gestao_de_laboratorios.com.br',
        ['erisson.c@escolar.ifrn.edu.br']
    )
    if estilo:
        estilo = estilo
        if estilo == 'table':
            chaves = [chaves[i:i + 10] for i in range(0, len(chaves), 10)]
            
    else:
        estilo = 'table'
        chaves = [chaves[i:i + 10] for i in range(0, len(chaves), 10)]
    
    contexto = {
        'chaves': chaves,
        'chaves_pegadas': chaves_pegadas,
        'estilo': estilo,
        'title': 'Chaves'
    }
    
    return render(
        request,
        'pegar_chave/pages/chaves.html',
        contexto,
    )


    


def adicionar_chave(request):
    form = forms.ChaveForm(request.POST or None)
    if request.method == "POST":
            if form.is_valid():
                chave = form.save(commit=False)
                chave.campus = request.user.campus
                chave.save()
                return redirect(reverse('pegar_chave:chaves'))
            

    contexto = {
        'form': form,
        'title': 'Adicionar Chave'
    }
    return render(request, 'pegar_chave/pages/chave_form.html', contexto)

def editar_chave(request, slug):
    chave = get_object_or_404(models.Chave, slug=slug)
    form = forms.ChaveForm(request.POST or None, instance=chave)
    if request.method == "POST":
            if form.is_valid():
                chave = form.save(commit=False)
                chave.save()
                return redirect(reverse('pegar_chave:chaves'))
            else:
                form = forms.ChaveForm(request.POST or None, instance=chave)
    contexto = {
        'form': form,
        'chave': chave,
        'title': f'Editar Chave {chave.bloco_num}'
    }
    return render(request, 'pegar_chave/pages/chave_form.html', contexto)

def deletar_chave(request, slug):
    chave = get_object_or_404(models.Chave, slug=slug)
    chave.delete()
    messages.success(request, f'Chave {chave.bloco_num} deletada com sucesso!')
    return redirect(reverse('pegar_chave:chaves'))
    

def pegar_chave(request, chave_slug, matricula_usuario=None):
    chave = get_object_or_404(models.Chave, slug=chave_slug)
    usuario = None
    
    if matricula_usuario:
        usuario = get_object_or_404(models.User, registration=matricula_usuario)

    matricula = request.GET.get('usuario')
    print(matricula)
    if matricula:
        usuario = models.User.objects.filter(registration=matricula)
        if usuario:
            return redirect(reverse('pegar_chave:confirmar_pegar_chave', kwargs={'chave_slug': chave.slug, 'matricula_usuario': matricula}))
        else:
            messages.error(request, f'O usuario da matrícula {matricula} não existe no banco de dados ou foi escrito errado, por favor, reescreva sua matrícula ou cadastre-se no app.')
            return redirect(reverse('pegar_chave:pegar_chave', kwargs={'chave_slug': chave.slug}))
    if request.method == "POST":
            form = forms.PegarChaveForm(request.POST)
            chave_pegada = form.save(commit=False)
            chave_pegada.usuario = usuario
            chave_pegada.chave = chave
            chave.situacao = 'em uso'
            chave_pegada.campus = request.user.campus
            chave.save()
            chave_pegada.save()
            return redirect(reverse('pegar_chave:visualizar_chave_pegada', kwargs={'slug': chave_pegada.slug}))
            

    contexto = {
        'usuario': usuario,
        'chave': chave,
        'title': f'Pegar Chave {chave}'
    }
    return render(request, 'pegar_chave/pages/pegar_chave_form.html', contexto)

def visualizar_chave_pegada(request, slug):
    chave_pegada = get_object_or_404(models.Pegar_Chave, slug=slug)

    contexto = {
        'chave_pegada': chave_pegada,
        'title': f'Visualizar Chave {chave_pegada.chave} Pegada por {chave_pegada.usuario}'
    }
    return render(request, 'pegar_chave/pages/visualizar_chave_pegada.html', contexto)

def devolver_chave_pegada(request, slug):
    chave_pegada = get_object_or_404(models.Pegar_Chave, slug=slug)
    chave = get_object_or_404(models.Chave, slug=chave_pegada.chave.slug)
    chave_pegada.situacao = 'devolvida'
    chave_pegada.save()
    chave.situacao = 'disponivel'
    chave.save()

    
    return redirect(reverse('pegar_chave:visualizar_chave_pegada', kwargs={'slug': chave_pegada.slug}))

def deletar_chave_pegada(request, slug):
    chave_pegada = get_object_or_404(models.Pegar_Chave, slug=slug)
    chave_pegada.delete()
    messages.success(request, f'Registro da chave {chave_pegada.chave} pegada por {chave_pegada.usuario} deletado com sucesso!')
    return redirect(reverse('pegar_chave:chaves'))