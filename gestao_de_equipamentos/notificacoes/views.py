from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from notifications.utils import slug2id


def notificacoes(request, categoria=None):
    if categoria == 'equipamentos':
        unread_notifications =  Notification.objects.unread().filter(Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento')) | Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='comment')) | Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='reply')) | Q(target_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento')), recipient=request.user)
    elif categoria == 'laboratorios':
        unread_notifications = Notification.objects.unread().filter(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='laboratorios', model='laboratorio'))
    elif categoria == 'tags':
        unread_notifications = Notification.objects.unread().filter(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='tags', model='tag'))
    elif categoria == 'denuncias':
        unread_notifications = Notification.objects.unread().filter(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='denuncias', model='denuncia'))
    elif categoria == 'chaves_reservs':
        unread_notifications = Notification.objects.unread().filter(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='chaves_reservs', model='chave_reserv'))
    else:
        unread_notifications = Notification.objects.unread().filter(recipient=request.user)
    contexto = {
        'title': 'Notificações',
        'notificacoes': unread_notifications,
        'categoria': categoria
    }
    return render(
        request,
        'notificacoes/pages/notificacoes.html',
        contexto,
    )
    
def mark_as_read(request, slug=None):
    notification_id = slug2id(slug)

    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()

    return redirect(reverse('notificacoes:notificacoes'))


def marcar_notificacoes_lidas(request, categoria=None):
    if categoria == 'equipamentos':
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento'))
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='comment'))
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='reply'))
    elif categoria == 'laboratorios':
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='laboratorios', model='laboratorio'))
    elif categoria == 'tags':
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='tags', model='tag'))
    elif categoria == 'denuncias':
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='denuncias', model='denuncia'))
    elif categoria == 'chaves_reservs':
        Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='chaves_reservs', model='chave_reserv'))
    else:
        Notification.objects.mark_all_as_read(recipient=request.user)
    return redirect(reverse('notificacoes:notificacoes'))

