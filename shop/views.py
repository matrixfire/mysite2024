from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from cart.forms import CartAddProductForm
from .models import Category, Product, Collection



def product_list(request, category_slug=None, collection_slug=None):
    category = None
    collection = None
    categories = Category.objects.annotate(total_products=Count('products'))
    collections = Collection.objects.annotate(total_products=Count('products'))
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collections=collection)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'collection': collection,
            'categories': categories,
            'collections': collections,
            'products': products,
        }
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.annotate(total_products=Count('products'))
    product_images = product.images.all()
    page_title = f"Reobrix-{product.name}"
    meta_description = f"Build your dreams with this Reobrix {product.name}!"
    
    product_tags_ids = product.tags.values_list('id', flat=True)
    similar_products = Product.objects.filter(
        tags__in=product_tags_ids, available=True
    ).exclude(id=product.id)
    similar_products = similar_products.annotate(same_tags=Count('tags')).order_by(
        '-same_tags', '-updated'
    )[:3]

    return render(
        request,
        'shop/product/detail.html',
        {
            'product': product,
            'categories': categories,
            'product_images': product_images,
            'page_title': page_title,
            'meta_description': meta_description,
            'similar_products': similar_products,
        }
    )
