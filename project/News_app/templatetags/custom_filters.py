from django import template
from ..models import Articles

register = template.Library()

@register.filter()
def currency(value):

   return f'{value} '