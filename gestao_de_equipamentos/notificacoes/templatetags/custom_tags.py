from django.template import Library
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

register = Library()

@register.inclusion_tag('global/partials/_sidebar.html')
def sidebar_view(user=None):
    unread_notifications_equips =  Notification.objects.unread().filter(Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='equipamento')) | Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='comment')) | Q(action_object_content_type=ContentType.objects.get(app_label='equipamentos', model='reply')), recipient=user).count()
    unread_notifications_labs = Notification.objects.unread().filter(recipient=user, action_object_content_type=ContentType.objects.get(app_label='laboratorios', model='laboratorio')).count()
    unread_notifications_tags = Notification.objects.unread().filter(recipient=user, action_object_content_type=ContentType.objects.get(app_label='tags', model='tag')).count()
    unread_notifications_notif = Notification.objects.unread().filter(recipient=user).count()
    context = {
        'notifications_equips': unread_notifications_equips,
        'notifications_labs': unread_notifications_labs,
        'notifications_tags': unread_notifications_tags,
        'notifications_notif': unread_notifications_notif,
        'user': user
    }
    return context