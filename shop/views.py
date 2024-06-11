from django.shortcuts import get_object_or_404, render

from cart.forms import CartAddProductForm
from .models import Category, Product
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




def product_list_(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        },
    )


def product_list(request, category_slug=None):
    category = None
    # categories = Category.objects.all()
    categories = Category.objects.annotate(total_products=Count('products'))
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Pagination with 3 products per page
    paginator = Paginator(products, 6)  # Adjust the number 6 to however many products per page you want
    page_number = request.GET.get('page', 1)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of results
        products = paginator.page(paginator.num_pages)

    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        },
    )



def product_detail(request, id, slug):
    product = get_object_or_404(
        Product, id=id, slug=slug, available=True
    )

    # List of similar products based on tags
    product_tags_ids = product.tags.values_list('id', flat=True)
    similar_posts = Product.objects.filter(
        tags__in=product_tags_ids, available=True
    ).exclude(id=product.id)
    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')
    ).order_by('-same_tags', '-updated')[:3]

    return render(
        request,
        'shop/product/detail.html',
        {'product': product, 'similar_posts': similar_posts}
    )