from django.http import HttpResponse
from .models import Slide, DIYNews

from django.shortcuts import render, get_object_or_404
from shop.models import Product, Collection
from blog.models import Post


# def index_(request):
#     """The home page for reobrix."""
#     slides = Slide.objects.all()
#     return render(request, 'core/index.html', {"slides": slides})



def index(request):
    new_arrivals_collection = get_object_or_404(Collection, slug="new-arrivals")
    popular_collection = get_object_or_404(Collection, slug="popular")

    new_arrivals = Product.objects.filter(collections=new_arrivals_collection, available=True).order_by('-created')[:4]
    popular_products = Product.objects.filter(collections=popular_collection, available=True).order_by('-created')[:4]

    slides = Slide.objects.all()  # Assuming you have a Slide model for slides
    diy_news_list = DIYNews.objects.all()  # Retrieve all DIYNews objects
    latest_classic_image_posts = Post.objects.filter(post_type=Post.PostType.CLASSIC_IMAGE).order_by('-created')[:4]  # Latest 4 classic image posts

    context = {
        'new_arrivals': new_arrivals,
        'popular_products': popular_products,
        'slides': slides,
        'diy_news_list': diy_news_list,
        'latest_classic_image_posts': latest_classic_image_posts,  # Add classic image posts to the context
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
