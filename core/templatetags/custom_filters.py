from django import template

register = template.Library()

@register.filter
def chunked(value, chunk_size):
    if not isinstance(value, list):
        raise TypeError('Expected a list')
    return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
