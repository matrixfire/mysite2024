# core/context_processors.py

from .models import BusinessInfo

def business_info(request):
    try:
        business_info = BusinessInfo.objects.first()
    except BusinessInfo.DoesNotExist:
        business_info = None
    
    return {
        'business_info': business_info
    }
