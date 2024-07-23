from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from notifications.utils import slug2id


def notificacoes(request):
    unread_notifications_equips =  Notification.objects.unread().filter(Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento')) | Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='comment')) | Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='reply')) | Q(target_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento')), recipient=request.user)
    unread_notifications_labs = Notification.objects.unread().filter(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='laboratorios', model='laboratorio'))
    unread_notifications_tags = Notification.objects.unread().filter(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='tags', model='tag'))
    contexto = {
        'title': 'Categorias',
        'notificacoes_equips': unread_notifications_equips,
        'notificacoes_labs': unread_notifications_labs,
        'notificacoes_tags': unread_notifications_tags
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

def marcar_notificacoes_lidas_equips(request):
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento'))
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='comment'))
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='reply'))
    return redirect(reverse('notificacoes:notificacoes'))

def marcar_notificacoes_lidas_labs(request):
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='laboratorios', model='laboratorio'))
    return redirect(reverse('notificacoes:notificacoes'))

def marcar_notificacoes_lidas_tags(request):
    Notification.objects.mark_all_as_read(recipient=request.user, action_object_content_type=ContentType.objects.get(app_label='tags', model='tag'))
    return redirect(reverse('notificacoes:notificacoes'))

def marcar_todas_notificacoes_lidas(request):
    Notification.objects.mark_all_as_read(recipient=request.user)
    return redirect(reverse('notificacoes:notificacoes'))

