from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from cart.forms import CartAddProductForm
from .models import Category, Product, Collection

from django.conf import settings


def product_list(request, category_slug=None, collection_slug=None):
    # Retrieve all categories and collections with the count of products in each
    category = None
    collection = None
    categories = Category.objects.annotate(total_products=Count('products'))
    collections = Collection.objects.annotate(total_products=Count('products'))
    products = Product.objects.filter(available=True)  # Filter available products

    # If a category slug is provided, filter products by that category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # If a collection slug is provided, filter products by that collection
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collections=collection)

    # Paginate the products list, using the value from settings
    products_per_page = getattr(settings, 'PRODUCTS_PER_PAGE', 6)  # Default to 6 if setting is not defined
    paginator = Paginator(products, products_per_page) 
    page_number = request.GET.get('page', 1)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)  # If page is not an integer, deliver first page
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page

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
    # Retrieve the product by id and slug, ensuring it is available
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.annotate(total_products=Count('products'))
    product_images = product.images.all()
    page_title = f"Reobrix-{product.name}"
    meta_description = f"Build your dreams with this Reobrix {product.name}!"

    # Find similar products based on tags, excluding the current product
    product_tags_ids = product.tags.values_list('id', flat=True)
    similar_products = Product.objects.filter(
        tags__in=product_tags_ids, available=True
    ).exclude(id=product.id)
    similar_products = similar_products.annotate(same_tags=Count('tags')).order_by(
        '-same_tags', '-updated'
    )[:3]  # Limit to 3 similar products

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
