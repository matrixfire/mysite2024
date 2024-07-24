# yourapp/templatetags/breadcrumbs.py
from django import template
from django.urls import resolve, reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def breadcrumbs(context):
    request = context['request']
    path = request.path
    parts = path.strip('/').split('/')
    
    breadcrumbs = []
    for i in range(len(parts)):
        url = '/' + '/'.join(parts[:i+1]) + '/'
        try:
            name = resolve(url).url_name
            breadcrumbs.append({'name': name, 'url': url})
        except:
            # If resolve fails, provide a default name based on the URL part
            name = parts[i].replace('-', ' ').title()
            breadcrumbs.append({'name': name, 'url': url})
    print(breadcrumbs)
    return breadcrumbs
