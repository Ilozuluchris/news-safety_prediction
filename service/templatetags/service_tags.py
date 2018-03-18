from django import template

register = template.Library()

@register.filter(name='my_enum')
def my_enum(value):
    return enumerate(value)