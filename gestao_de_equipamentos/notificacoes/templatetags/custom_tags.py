from django.template import Library

register = Library()

@register.inclusion_tag('global/partials/_sidebar.html')
def sidebar_view(user=None):
    context = {
        'user': user
    }
    return context