from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
import json
from laboratorios import forms, models
from django.contrib import messages
from django.db.models import ProtectedError
from django.db import IntegrityError
from notifications.models import Notification
from notifications.signals import notify
from usuarios.models import User

    
def laboratorios(request):
    if not request.user.is_authenticated:
        return redirect(reverse('usuarios:login'))
    laboratorios = models.Laboratorio.objects.filter(campus=request.user.campus)
    contexto = {
        'laboratorios': laboratorios,
        'title': 'Laboratórios'
    }
    return render(
        request,
        'laboratorios/pages/laboratorios.html',
        contexto,
    )


    
def laboratorio_list(request):
    laboratorios = models.Laboratorio.objects.filter(campus=request.user.campus)
    unread_notifications_labs_adicionar = Notification.objects.unread().filter(recipient=request.user, verb='Novo Laboratório!')
    unread_notifications_labs_update = {}
    for labs in laboratorios:
        unread_notifications_labs_update.update({labs:Notification.objects.unread().filter(recipient=request.user, verb='Laboratório Atualizado!', action_object_object_id=labs.id).count()})
    notificacoes = {
        'unread_notifications_labs_adicionar': unread_notifications_labs_adicionar,
        'unread_notifications_labs_update': unread_notifications_labs_update
    }
    contexto = {
        'notificacoes': notificacoes,
        'laboratorios': laboratorios,
        'title': 'Laboratorios'
    }
    return render(request, 'laboratorios/pages/laboratorio_list.html',
        contexto,
    )

def marcar_notificacao_laboratorio_lida(request):
    laboratorios = models.Laboratorio.objects.filter(campus=request.user.campus)
    for laboratorio in laboratorios:
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_object_id=laboratorio.id)
    return HttpResponse(status=204)

def adicionar_laboratorio(request):
    form = forms.LaboratorioForm(request.POST or None)
    if request.method == "POST":
            if form.is_valid():
                laboratorio = form.save(commit=False)
                laboratorio.campus = request.user.campus
                laboratorio.save()
                usuarios = list(User.objects.filter(campus=request.user.campus))
                notify.send(request.user, recipient=usuarios, verb='Novo Laboratório!', description=f'O laboratório {laboratorio.nome} foi adicionado', action_object=laboratorio)
                return redirect(reverse('laboratorios:laboratorios'))
            

    contexto = {
        'form': form,
        'title': 'Adicionar Laboratório'
    }
    return render(request, 'laboratorios/pages/laboratorio_form.html', contexto)


def visualizar_laboratorio(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    
    dia_sem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    turno = ['Matutino', 'Vespertino', 'Noturno']
    horas = [1, 2, 3, 4, 5, 6]
    
    HORARIOS = []
    
    for Dia_sem in dia_sem:
        for Turno in turno:
            for Horas in horas:
                if Turno != 'Noturno' or Horas != 6:
                    HORARIOS.append(f'{Dia_sem};{Turno};{Horas}',)
                    
    Horarios = []
    
    if laboratorio.horarios:
        for horario in laboratorio.horarios.all():
            for Dia_sem in dia_sem:
                for Turno in turno:        
                    for Horario in horario.horario:
                        if Horario.split(';')[0] == Dia_sem and Horario.split(';')[1] == Turno:
                            Horarios.append({'id': horario.id, 'dia_sem_turno': f'{Horario.split(';')[0]}, {Horario.split(';')[1]}', 'horas': Horario.split(';')[2]})
                    
    contexto = {
        'laboratorio': laboratorio,
        'HORARIOS': HORARIOS,
        'Horarios': Horarios,
        'title': f'Visualizar equipamentos de {laboratorio.nome}'
    }
    return render(request, 'laboratorios/pages/visualizar_laboratorio.html', contexto)


def editar_laboratorio(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.LaboratorioForm(request.POST or None, instance=laboratorio)
    if request.method == "POST":
        try:
            if form.is_valid():
                laboratorio = form.save()
                usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
                notify.send(request.user, recipient=usuarios, verb='Laboratório Atualizado!', description=f'O laboratório {laboratorio.nome} foi atualizado', action_object=laboratorio )
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        except IntegrityError:
            messages.error(request, (f'{laboratorio.nome} já existe no campus {laboratorio.campus}!'))
    contexto = {
        'form': form,
        'laboratorio': laboratorio,
        'title': f'Editar {laboratorio.nome}'
    }
    return render(request, 'laboratorios/pages/laboratorio_form.html', contexto)


def adicionar_horario(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.HorarioForm(request.POST or None)
    
    dia_sem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    turno = ['Matutino', 'Vespertino', 'Noturno']
    horas = [1, 2, 3, 4, 5, 6]

    HORARIO = []
    
    for Dia_sem in dia_sem:
        for Turno in turno:
            for Horas in horas:
                if Turno != 'Noturno' or Horas != 6:
                    HORARIO.append(f'{Dia_sem};{Turno};{Horas}',)
    
    
    if request.method == "POST":

            if form.is_valid():
                horario_aula = form.save(commit=False)
                horario_aula.autor = request.user
                horario_aula.laboratorio = laboratorio
                horarios = request.POST.getlist('horario')
                horario_aula.horario = horarios
                horario_aula.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'horarios': HORARIO,
        'form': form,
        'title': 'Adicionar Horário'
    }
    return render(request, 'laboratorios/pages/horarios_form.html', contexto)

def adicionar_professor(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.ProfessorForm(request.POST or None)
    print(form)
    
    if request.method == "POST":

            if form.is_valid():
                professor = form.save(commit=False)
                professor.laboratorio = laboratorio
                professor.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'form': form,
        'title': 'Adicionar Professor'
    }
    return render(request, 'laboratorios/pages/professores_form.html', contexto)

def adicionar_projeto(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.ProjetoForm(request.POST or None)

    
    if request.method == "POST":

            if form.is_valid():
                professor = form.save(commit=False)
                professor.laboratorio = laboratorio
                professor.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'form': form,
        'title': 'Adicionar Projeto'
    }
    return render(request, 'laboratorios/pages/projeto_form.html', contexto)

def adicionar_servico(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.ServicoForm(request.POST or None)

    
    if request.method == "POST":

            if form.is_valid():
                professor = form.save(commit=False)
                professor.laboratorio = laboratorio
                professor.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'form': form,
        'title': 'Adicionar Serviço'
    }
    return render(request, 'laboratorios/pages/servicos_form.html', contexto)

def adicionar_equipamento(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.EquipamentoForm(request.POST or None)

    
    if request.method == "POST":

            if form.is_valid():
                professor = form.save(commit=False)
                professor.laboratorio = laboratorio
                professor.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'form': form,
        'title': 'Adicionar Equipamento'
    }
    return render(request, 'laboratorios/pages/equipamento_form.html', contexto)

def adicionar_material(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.MaterialForm(request.POST or None)

    
    if request.method == "POST":

            if form.is_valid():
                professor = form.save(commit=False)
                professor.laboratorio = laboratorio
                professor.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'form': form,
        'title': 'Adicionar Material'
    }
    return render(request, 'laboratorios/pages/material_form.html', contexto)

def adicionar_foto(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    form = forms.FotoForm(request.POST or None)

    
    if request.method == "POST":

            if form.is_valid():
                professor = form.save(commit=False)
                professor.laboratorio = laboratorio
                professor.save()
                return redirect(reverse('laboratorios:visualizar_laboratorio',  kwargs={'slug': slug}))
        
            else:
                print(form.errors)
    contexto = {
        'form': form,
        'title': 'Adicionar Foto'
    }
    return render(request, 'laboratorios/pages/foto_form.html', contexto)


def remover_laboratorio(request, slug):
    laboratorio = get_object_or_404(models.Laboratorio, slug=slug)
    laboratorio.delete()
    messages.success(request, f'Laboratório {laboratorio.nome} deletado com sucesso!')
    return redirect(reverse('pegar_chave:chaves'))
