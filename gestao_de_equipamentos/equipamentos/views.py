from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from equipamentos import forms
from equipamentos.models import Equipamento, Comment, Reply, Tag, Laboratorio
from notifications.signals import notify
from usuarios.models import User
from django.db.models import Q
from notifications.models import Notification

    

def autocomplete(request):
    if 'term' in request.GET:
        filter = request.GET.get('filter')
        qs = Equipamento.objects.filter(laboratorio__campus=request.user.campus, titulo__icontains=request.GET.get('term'), laboratorio__slug=filter)
        titulos = list()
        for equipamento in qs:
            titulos.append(equipamento.titulo)
        return JsonResponse(titulos, safe=False)

def equipamentos(request):
    if not request.user.is_authenticated:
        return redirect(reverse('usuarios:login'))
    contexto = {}
    laboratorios = Laboratorio.objects.filter(campus=request.user.campus)
    tags = Tag.objects.all()
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tag = request.GET.get('tags_filtro')
    if filter:
        if tag and search:
            equipamentos = Equipamento.objects.filter(laboratorio__campus=request.user.campus, tags__slug=tag, titulo__icontains=search, laboratorio__slug=filter)
        elif tag:
            equipamentos = Equipamento.objects.filter(laboratorio__campus=request.user.campus, tags__slug=tag, laboratorio__slug=filter)
        elif search:
            equipamentos = Equipamento.objects.filter(laboratorio__campus=request.user.campus, titulo__icontains=search, laboratorio__slug=filter)
        else:
            equipamentos = Equipamento.objects.filter(laboratorio__campus=request.user.campus, laboratorio__slug=filter)
    else:
        equipamentos = Equipamento.objects.filter(laboratorio__campus=request.user.campus)
    
    unread_notifications_equips_update = {}
    unread_notifications_comments_replies_add = {}
    unread_notifications_comments_replies_update = {}
    for equips in equipamentos:
        unread_notifications_replies_add = unread_notifications_replies_update = 0
        unread_notifications_comments_add = Notification.objects.unread().filter(verb='Novo Comentário!', recipient=request.user, target_object_id=equips.id).count()
        unread_notifications_comments_update = Notification.objects.unread().filter(verb='Comentário Atualizado!', recipient=request.user, target_object_id=equips.id).count()
        unread_notifications_equips_update.update({equips:Notification.objects.unread().filter(verb='Equipamento Atualizado!', recipient=request.user, action_object_object_id=equips.id).count(),})
        for comment in equips.comments.all():
            unread_notifications_replies_add += Notification.objects.unread().filter(verb='Nova Resposta!', recipient=request.user, target_object_id=comment.id).count()
            unread_notifications_replies_update += Notification.objects.unread().filter(verb='Resposta Atualizada!', recipient=request.user, target_object_id=comment.id).count()
        unread_notifications_comments_replies_add.update({equips:unread_notifications_comments_add+unread_notifications_replies_add,})
        unread_notifications_comments_replies_update.update({equips:unread_notifications_comments_update+unread_notifications_replies_update,})
        
    unread_notifications_equips_add = Notification.objects.unread().filter(recipient=request.user, verb='Novo Equipamento!')
    
    notificacoes = {'unread_notifications_comments_replies_add': unread_notifications_comments_replies_add,
                    'unread_notifications_comments_replies_update': unread_notifications_comments_replies_update,
                    'unread_notifications_equips_add': unread_notifications_equips_add,
                    'unread_notifications_equips_update': unread_notifications_equips_update}
    
    paginator = Paginator(equipamentos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
                                
    contexto.update({
        'equipamentos': page_obj,
        'laboratorios': laboratorios,
        'tags': tags,
        'notificacoes': notificacoes,
        'title': 'Equipamentos'
    })
    return render(
        request,
        'equipamentos/pages/equipamentos.html',
        contexto,
    )
    

def visualizar_equipamento(request, slug):
    equipamento = get_object_or_404(Equipamento, slug=slug)
    unread_notifications_comments_add = Notification.objects.unread().filter(recipient=request.user, verb='Novo Comentário!', target_object_id=equipamento.id)
    unread_notifications_equips_add = Notification.objects.unread().filter(recipient=request.user, verb='Novo Equipamento!', action_object_object_id=equipamento.id)
    unread_notifications_equips_update = Notification.objects.unread().filter(recipient=request.user, verb='Equipamento Atualizado!', action_object_object_id=equipamento.id).count()
    unread_notifications_replies_add = list()
    unread_notifications_comments_update = {}
    unread_notifications_replies_update = {}
    unread_notifications_comments_replies_add = {}
    unread_notifications_comments_replies_update = {}
    for comment in equipamento.comments.all():
        unread_notifications_replies_add.append(Notification.objects.unread().filter(recipient=request.user,verb='Nova Resposta!', target_object_id=comment.id))
        unread_notifications_comments_update.update({comment:Notification.objects.unread().filter(recipient=request.user, verb='Comentário Atualizado!', target_object_id=equipamento.id, action_object_object_id=comment.id).count(),})
        unread_notifications_comments_replies_add.update({comment:Notification.objects.unread().filter(verb='Nova Resposta!', recipient=request.user, target_object_id=comment.id).count(),})
        unread_notifications_comments_replies_update.update({comment:Notification.objects.unread().filter(verb='Resposta Atualizada!', recipient=request.user, target_object_id=comment.id).count(),})
        for reply in comment.replies.all():
            unread_notifications_replies_update.update({reply:Notification.objects.unread().filter(recipient=request.user,verb='Resposta Atualizada!', target_object_id=comment.id, action_object_object_id=reply.id).count(),})
            
    notificacoes = {
        'unread_notifications_comments_add': unread_notifications_comments_add,
        'unread_notifications_replies_add': unread_notifications_replies_add,
        'unread_notifications_equips_add': unread_notifications_equips_add,
        'unread_notifications_comments_update': unread_notifications_comments_update,
        'unread_notifications_replies_update': unread_notifications_replies_update,
        'unread_notifications_equips_update': unread_notifications_equips_update,
        'unread_notifications_comments_replies_add': unread_notifications_comments_replies_add,
        'unread_notifications_comments_replies_update': unread_notifications_comments_replies_update,
    }
    
    
    commentform = forms.CommentCreateForm()
    replyform = forms.ReplyCreateForm()
    contexto={
        'equipamento': equipamento,
        'notificacoes': notificacoes,
        'commentform' : commentform,
        'replyform' : replyform,
        'title': f'Visualizar Equipamento - {equipamento.titulo}'
    }
    return render(
        request,
        'equipamentos/pages/visualizar-equipamento.html',
        contexto
    )
    
    
def marcar_notificacao_lida(request, slug):
    equipamento = get_object_or_404(Equipamento, slug=slug)
    Notification.objects.mark_all_as_read(recipient=request.user, target_object_id=equipamento.id)
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_object_id=equipamento.id)
    for comment in equipamento.comments.all():
        Notification.objects.mark_all_as_read(recipient=request.user, target_object_id=comment.id)
    return HttpResponse(status=204)

def comment_status(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    replyform = forms.ReplyCreateForm()
    if request.method == 'POST':
        if comment.status == False:
            comment.status = True
        else:
            comment.status = False
        comment.save()
        usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
        notify.send(comment.author, recipient=usuarios, verb='Comentário Atualizado!', description=f'O comentário {comment.body} de {comment.author} foi atualizado', target=comment.parent_post, action_object=comment )
    context = {
                'comment': comment,
                'replyform': replyform
               }
    return render(request, 'equipamentos/pages/comment.html', context)
        

def reply_status(request, pk):
    reply = get_object_or_404(Reply, id=pk)
    if request.method == 'POST':
        if reply.status == False:
            reply.status = True
        else:
            reply.status = False
        reply.save()
        usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
    notify.send(reply.author, recipient=usuarios, verb='Resposta Atualizada!', description=f'A resposta {reply.body} de {reply.author} foi atualizada', target=reply.parent_comment, action_object=reply )
    context = {
                'reply': reply,
               }
    return render(request, 'equipamentos/pages/reply.html', context)
        

def comment_sent(request, pk):
    equipamento = get_object_or_404(Equipamento, id=pk)
    replyform = forms.ReplyCreateForm()
    if request.method == 'POST':
        form = forms.CommentCreateForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = equipamento
            comment.save()
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(comment.author, recipient=usuarios, verb='Novo Comentário!', description=f'O comentário {comment.body} de {comment.author} foi adicionado', target=equipamento, action_object=comment)
            
    context = {
        'equipamento' : equipamento,
        'comment': comment,
        'replyform': replyform
    }

    return render(request, 'equipamentos/pages/snippets/add_comment.html', context)

def denunciar_comentario(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    usuarios = list(User.objects.filter(Q(link_type='Servidor') | Q(is_admin=True), campus=request.user.campus))
    notify.send(request.user, level=Notification.LEVELS.error, recipient=usuarios, verb='Comentário Denunciado!', description=f'O comentário {comment.body} de {comment.author} foi Denunciado por {request.user}', target=comment.parent_post, action_object=comment)
    return HttpResponse(status=204)

def comment_edit(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    replyform = forms.ReplyCreateForm()
    form = forms.CommentCreateForm(request.POST or None, instance=comment)
    context = {
        'replyform': replyform,
        'form': form,
        'comment': comment
    }
    if request.method == 'POST':
        if form.is_valid:
            comment = form.save()
            context.update({
                'form': None,
                'comment': comment
            })
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(comment.author, recipient=usuarios, verb='Comentário Atualizado!', description=f'O comentário {comment.body} de {comment.author} foi atualizado', target=comment.parent_post, action_object=comment)
            
    return render(request, 'equipamentos/pages/comment.html', context)

def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    replyform = forms.ReplyCreateForm()
    if request.method == 'POST':
        form = forms.ReplyCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(reply.author, recipient=usuarios, verb='Nova Resposta!', description=f'A resposta {reply.body} de {reply.author} foi adicionada', target=comment, action_object=reply )
            
    context = {
        'reply' : reply,
        'comment': comment,
        'replyform': replyform
    }

    return render(request, 'equipamentos/pages/snippets/add_reply.html', context)

def denunciar_resposta(request, pk):
    reply = get_object_or_404(Reply, id=pk)
    usuarios = list(User.objects.filter(Q(link_type='Servidor') | Q(is_admin=True), campus=request.user.campus))
    notify.send(request.user, level=Notification.LEVELS.error, recipient=usuarios, verb='Resposta Denunciada!', description=f'A resposta {reply.body} de {reply.author} foi Denunciado por {request.user}', target=reply.parent_comment, action_object=reply)
    return HttpResponse(status=204)

def reply_edit(request, pk):
    reply = get_object_or_404(Reply, id=pk)
    form = forms.ReplyCreateForm(request.POST or None, instance=reply)
    context = {
        'form': form,
        'reply': reply
    }
    if request.method == 'POST':
        if form.is_valid:
            reply = form.save()
            context.update({
                'form': None,
                'reply': reply
            })
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(reply.author, recipient=usuarios, verb='Resposta Atualizada!', description=f'A resposta {reply.body} de {reply.author} foi atualizada', target=reply.parent_comment, action_object=reply )
            
    return render(request, 'equipamentos/pages/reply.html', context)

def comment_delete_view(request, pk):
    comment = get_object_or_404(Comment, id=pk, author=request.user)
    
    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Comentário deletado')
        usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
        notify.send(request.user, recipient=usuarios, verb='Comentário Deletado!', description=f'O comentário {comment.body} de {comment.author} foi deletado', target=comment.parent_post, action_object=comment)
        return redirect('equipamentos:visualizar_equipamento', comment.parent_post.slug )
    contexto = {
        'title': f'Deletar Comentário - {comment.body}',
        'comment': comment
    }
    
    return render(request, 'equipamentos/pages/comment_delete.html', contexto)


def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    
    if request.method == "POST":
        reply.delete()
        messages.success(request, 'Resposta deletada!')
        usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
        notify.send(request.user, recipient=usuarios, verb='Resposta Deletada!', description=f'A resposta {reply.body} de {reply.author} foi deletada', target=reply.parent_comment, action_object=reply)
        return redirect('equipamentos:visualizar_equipamento', reply.parent_comment.parent_post.slug )
        
    contexto = {
        'title': f'Deletar Resposta - {reply.body}',
        'reply' : reply
    }
    
    return render(request, 'equipamentos/pages/reply_delete.html', contexto)


def adicionar_equipamento(request):
    form = forms.EquipamentoForm(request.POST or None, request.FILES or None)
    contexto = {
        'title': 'Adicionar Equipamento',
        'form': form
    }
    if request.POST:
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            form.save_m2m()
            messages.success(request, f'{equipamento.titulo} criado com sucesso.')
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(request.user, recipient=usuarios, verb='Novo Equipamento!', description=f'O equipamento {equipamento.titulo} foi adicionado', action_object=equipamento )
            return redirect(reverse('equipamentos:equipamentos'))
    return render(
        request,
        'equipamentos/pages/equipamentos_form.html',
        contexto
    )
    


def editar_equipamento(request, slug):
    equipamento = get_object_or_404(Equipamento, slug=slug)
    form = forms.EquipamentoForm(request.POST or None, request.FILES or None, instance=equipamento)
    if request.POST:
        if form.is_valid():
            equipamento = form.save()
            messages.success(request, f'{equipamento.titulo} editado com sucesso.')
            usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
            notify.send(request.user, recipient=usuarios, verb='Equipamento Atualizado!', description=f'O equipamento {equipamento.titulo} foi atualizado', action_object=equipamento)
            return redirect(reverse('equipamentos:visualizar_equipamento',  kwargs={'slug': slug}))
        equipamento = get_object_or_404(Equipamento, slug=slug)
    contexto = {
        'title': f'Editar Equipamento - {equipamento.titulo}',
        'equipamento': equipamento,
        'form': form
    }
    return render(request, 'equipamentos/pages/equipamentos_form.html', contexto)
    


def remover_equipamento(request, slug):
    equipamento = get_object_or_404(Equipamento, slug=slug)
    
    if request.method == "POST":
        equipamento.delete()
        messages.success(request, f'{equipamento.titulo} deletado')
        usuarios = list(User.objects.filter(campus=request.user.campus).exclude(registration=request.user.registration))
        notify.send(request.user, recipient=usuarios, verb='Equipamento Deletado!', description=f'O equipamento {equipamento.titulo} foi deletado', action_object=equipamento)
        return redirect('equipamentos:equipamentos')
    
    contexto = {
        'title': f'Deletar Equipamento - {equipamento.titulo}',
        'equipamento' : equipamento
    }    
    
    return render(request, 'equipamentos/pages/equipamento_delete.html', contexto)


