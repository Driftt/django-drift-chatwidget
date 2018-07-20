from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('drift_chatwidget/js_snippet.html', takes_context=True, name='drift_chatwidget')
def chat_widget(context):
    widget_settings = settings.DRIFT_CHAT_WIDGET
    context['drift_widget_code'] = widget_settings.get('ID')
    context['drift_snippet_version'] = widget_settings.get('SNIPPET_VERSION')
    return context
