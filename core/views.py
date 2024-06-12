from django.http import HttpResponse
from .models import Slide

from django.shortcuts import render, get_object_or_404
from shop.models import Product, Collection


# def index_(request):
#     """The home page for reobrix."""
#     slides = Slide.objects.all()
#     return render(request, 'core/index.html', {"slides": slides})


def index(request):
    print("FUCK!")
    new_arrivals_collection = get_object_or_404(Collection, slug="new-arrivals")
    popular_collection = get_object_or_404(Collection, slug="popular")

    new_arrivals = Product.objects.filter(collections=new_arrivals_collection, available=True).order_by('-created')[:4]
    popular_products = Product.objects.filter(collections=popular_collection, available=True).order_by('-created')[:4]
    print(f'Len is {len(new_arrivals)}'*100)

    slides = Slide.objects.all()  # Assuming you have a Slide model for slides

    context = {
        'new_arrivals': new_arrivals,
        'popular_products': popular_products,
        'slides': slides,
    }
    return render(request, 'core/index.html', context)




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


# def index(request):
#     return render(request, 'core/index.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def search_results(request):
    return render(request, 'core/search-results.html')


def shop(request):
    return render(request, 'core/shop.html')


def single_product(request):
    return render(request, 'core/single-product.html')
