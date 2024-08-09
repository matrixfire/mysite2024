# core/middleware/redirect_middleware.py
from django.http import HttpResponsePermanentRedirect

class RedirectToWWWMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if not host.startswith('www.'):
            new_url = request.build_absolute_uri(request.get_full_path())
            new_url = new_url.replace(f"http://{host}", f"http://www.{host}")
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)
