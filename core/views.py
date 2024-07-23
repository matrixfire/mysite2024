from django.http import HttpResponse
from .models import Slide
from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, Collection
from blog.models import Post


from taggit.models import Tag
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank



from .tasks import test, fucking_print



from django.contrib import messages
from .forms import SubscriberForm



def index(request):
    try:
        new_arrivals_collection = get_object_or_404(Collection, slug="new-arrivals")
    except Http404:
        new_arrivals_collection = None

    try:
        popular_collection = get_object_or_404(Collection, slug="popular")
    except Http404:
        popular_collection = None

    if new_arrivals_collection:
        new_arrivals = Product.objects.filter(collections=new_arrivals_collection, available=True).order_by('-created')[:]
    else:
        new_arrivals = []

    if popular_collection:
        popular_products = Product.objects.filter(collections=popular_collection, available=True).order_by('-created')[:4]
    else:
        popular_products = []

    slides = Slide.objects.all()  # Assuming you have a Slide model for slides
    slide_count = slides.count()


    latest_featured_image_posts = Post.objects.filter(tags__name__in=["homepage_post"]).order_by('-created')
    
    # Ensure latest_classic_image_posts has exactly 4 items
    # if latest_classic_image_posts.count() < 4:
    #     # Repeat the last item to fill up to 4 items
    #     if latest_classic_image_posts.exists():
    #         last_post = latest_classic_image_posts.last()
    #         remaining_posts_needed = 4 - latest_classic_image_posts.count()
    #         for _ in range(remaining_posts_needed):
    #             latest_classic_image_posts = latest_classic_image_posts | Post.objects.filter(pk=last_post.pk)
    #     else:
    #         latest_classic_image_posts = Post.objects.none()

    latest_featured_image_posts = latest_featured_image_posts[:4]  # Limit to 4 items

    upcoming_products_blog_list = Post.objects.filter(tags__name__in=["upcoming_products"])
    


    context = {
        'new_arrivals': new_arrivals,
        'popular_products': popular_products,
        'slides': slides,
        'latest_featured_image_posts': latest_featured_image_posts,
        'upcoming_products_blog_list': upcoming_products_blog_list,        
    }
    return render(request, 'core/index.html', context)





def about_us(request):
    # f("fuckfuckfuck")
    # launch asynchronous task
    # print(f"fucking test111")
    # try:
    #     test.delay("tesing this celery rabbitmq...")
    # except:
    #     print("Celery...failed.")
    print(f"fucking test2")
    return render(request, 'core/about-us.html')


def blog_single_post(request):
    return render(request, 'core/blog-single-post.html')


def blog(request):
    return render(request, 'core/blog.html')


def checkout(request):
    return render(request, 'core/checkout.html')


def contacts(request):
    return render(request, 'core/contacts.html')



def join_us(request):
    return render(request, 'core/join-us.html')


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




def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = SubscriberForm()

    return render(request, 'subscribe.html', {'form': form})
