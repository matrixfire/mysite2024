from django.http import HttpResponse
from .models import Slide, DIYNews
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from shop.models import Product, Collection
from blog.models import Post



from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank
)


# def index_(request):
#     """The home page for reobrix."""
#     slides = Slide.objects.all()
#     return render(request, 'core/index.html', {"slides": slides})

# new_arrivals, popular_products = None, None



def index(request):
    try:
        new_arrivals_collection = get_object_or_404(Collection, slug="new-arrivals")
        # print(new_arrivals_collection.count) # ???
    except Http404:
        new_arrivals_collection = None

    try:
        popular_collection = get_object_or_404(Collection, slug="popular")
    except Http404:
        popular_collection = None

    if new_arrivals_collection:
        new_arrivals = Product.objects.filter(collections=new_arrivals_collection, available=True).order_by('-created')[:4]
    else:
        new_arrivals = []

    if popular_collection:
        popular_products = Product.objects.filter(collections=popular_collection, available=True).order_by('-created')[:4]
    else:
        popular_products = []

    slides = Slide.objects.all()  # Assuming you have a Slide model for slides
    slide_count = slides.count()
    print(f"Number of slides: {slide_count}")

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



from .tasks import test

def f(name):
    print("testing before")
    test(name)
    print("testing after")





def about_us(request):
    # f("fuckfuckfuck")
    # launch asynchronous task
    test.delay("tesing this celery rabbitmq...")
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


class SearchForm(forms.Form):
    query = forms.CharField()


def search(request, queryset, search_fields):
    form = SearchForm()
    query = None
    results = queryset.none()

    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            print(query, type(query))
            search_vector = SearchVector(*search_fields)
            print(*search_fields)
            results = queryset.annotate(search=search_vector).filter(search=query)
    
    paginator = Paginator(results, 3)  # Paginate with 3 items per page
    page_number = request.GET.get('page', 1)

    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, get the first page
        items = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range, get the last page of results
        items = paginator.page(paginator.num_pages)

    return render(
        request,
        'shop/product/list.html',
        {
            'products': items,
            'query': query,
            'form': form,
        }


        # {
        #     'category': category,
        #     'collection': collection,
        #     'categories': categories,
        #     'collections': collections,
        #     'products': products,
        # }
    )




def search_results(request):
    queryset = Product.objects.filter(available=True)
    print(f'{len(queryset)}')
    search_fields = ['name', 'description', 'short_description']
    return search(request, queryset, search_fields)
    # return render(request, 'core/search-results.html')


def shop(request):
    return render(request, 'core/shop.html')


def single_product(request):
    return render(request, 'core/single-product.html')
