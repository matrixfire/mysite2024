from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide

def index(request):
    """The home page for reobrix."""
    slides = Slide.objects.all()
    return render(request, 'core/index.html', {"slides": slides})

def about(request):
    return render(request, 'core/about.html')




def programs(request):
    return render(request, 'core/programs.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def faq(request):
    return render(request, 'core/faq.html')

def reviews(request):
    return render(request, 'core/reviews.html')

def contacts(request):
    return render(request, 'core/contacts.html')


def search_results(request):
    return render(request, 'core/search-results.html')

def single_program(request):
    return render(request, 'core/single-program.html')