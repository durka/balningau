import snudown
from django import template
register = template.Library()

@register.filter
def markdown(value):
    return snudown.markdown(value)

