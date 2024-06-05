from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide

def index(request):
    """The home page for reobrix."""
    slides = Slide.objects.all()
    return render(request, 'core/index.html', {"slides": slides})

def about_us(request):
    return render(request, 'core/about-us.html')


def blog_single_post(request):
    return render(request, 'core/blog-single-post.html')


def blog(request):
    return render(request, 'core/blog.html')


def checkout(request):
    return render(request, 'core/checkout.html')


def contacts(request):
    return render(request, 'core/contacts.html')


def index(request):
    return render(request, 'core/index.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def search_results(request):
    return render(request, 'core/search-results.html')


def shop(request):
    return render(request, 'core/shop.html')


def single_product(request):
    return render(request, 'core/single-product.html')
