from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import json
from tags import forms, models
from equipamentos.models import Equipamento
from notifications.models import Notification
from notifications.signals import notify
from usuarios.models import User
from django.contrib.contenttypes.models import ContentType


def tags(request):
    contexto = {
        'title': 'Categorias'
    }
    return render(
        request,
        'tags/pages/tags.html',
        contexto,
    )


    
def tags_list(request):
    tags = models.Tag.objects.all()
    unread_notifications_tags_add = Notification.objects.unread().filter(recipient=request.user, verb='Nova Categoria!')
    unread_notifications_tags_update = {}
    for tag in tags:
        unread_notifications_tags_update.update({tag:Notification.objects.unread().filter(recipient=request.user, verb='Categoria Atualizada!', action_object_object_id=tag.id).count()})
    notificacoes = {
        'unread_notifications_tags_add': unread_notifications_tags_add,
        'unread_notifications_tags_update': unread_notifications_tags_update
    }
    contexto = {
        'tags': tags,
        'notificacoes': notificacoes,
        'title': 'Categorias'
    }
    return render(request, 'tags/pages/tags_list.html',
        contexto,
    )


def marcar_notificacao_tag_lida(request):
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='tags', model='tag'))
    return HttpResponse(status=204)

def tag_create(request):
    form = forms.TagForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            tag = form.save()
            usuarios = list(User.objects.filter(campus=request.user.campus))
            notify.send(request.user, recipient=usuarios, verb='Nova Categoria!', description=f'A categoria {tag.nome} foi adicionada', action_object=tag )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "tagsListChanged": None,
                        "showMessage": f"Categoria {tag.nome} adicionada."
                    })
                })
    contexto = {
        'title': 'Criar categoria',
        'form': form,
    }
    return render(request, 'tags/pages/tag_form.html', contexto)

def view_equipamentos_tag(request, slug):
    tag = get_object_or_404(models.Tag, slug=slug)
    equipamentos = Equipamento.objects.filter(tags=tag)
    contexto = {
        'equipamentos': equipamentos,
        'tag': tag,
        'title': f'Visualizar equipamentos de {tag.nome}'
    }
    return render(request, 'tags/pages/view_equipamentos_tag.html', contexto)


def tag_edit(request, slug):
    tag = get_object_or_404(models.Tag, slug=slug)
    form = forms.TagForm(request.POST or None, request.FILES or None, instance=tag)
    if request.method == "POST":
        if form.is_valid():
            tag = form.save()
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(request.user, recipient=usuarios, verb='Categoria Atualizada!', description=f'A categoria {tag.nome} foi editada', action_object=tag )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "tagsListChanged": None,
                        "showMessage": f"Categoria {tag.nome} atualizada."
                    })
                })
    contexto = {
        'form': form,
        'tag': tag,
        'title': f'Editar {tag.nome}'
    }
    return render(request, 'tags/pages/tag_form.html', contexto)

def tag_delete(request, slug):
    tag = get_object_or_404(models.Tag, slug=slug)
    if request.method == "POST":
        tag.delete()
        usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
        notify.send(request.user, recipient=usuarios, verb='Categoria Deletada!', description=f'A categoria {tag.nome} foi deletada', action_object=tag)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "tagsListChanged": None,
                    "showMessage": f"Categoria {tag.nome} deletada."
                })
            }) 
    contexto = {
        'title': f'Deletar {tag.nome}',
        'tag': tag
    }
    return render(request, 'tags/pages/tag_delete.html', contexto)