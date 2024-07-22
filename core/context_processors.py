# core/context_processors.py
from django.urls import resolve

from .models import BusinessInfo

def business_info(request):
    try:
        business_info = BusinessInfo.objects.first()
    except BusinessInfo.DoesNotExist:
        business_info = None
    
    return {
        'business_info': business_info
    }




def current_view_name(request):
    current_url = resolve(request.path_info)
    return {
        'current_view_name': current_url.url_name
    }