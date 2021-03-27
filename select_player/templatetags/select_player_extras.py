from django import template

register = template.Library()


@register.filter
def get_attr(object, name):
    return getattr(object, name, '')