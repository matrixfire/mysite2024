from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from taggit.models import Tag

from .forms import EmailPostForm, SearchForm
from .models import Post
from django.conf import settings


def post_list(request, tag_slug=None):
    # Retrieve all published posts
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        # Filter posts by the given tag
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    
    # Paginate the posts list, using the value from settings
    posts_per_page = getattr(settings, 'POSTS_PER_PAGE', 3)  # Default to 6 if setting is not defined
    paginator = Paginator(post_list, posts_per_page)
    page_number = request.GET.get('page', 1)

    tags = Tag.objects.all()  # Get all tags
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range, get last page of results
        posts = paginator.page(paginator.num_pages)
    
    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'tag': tag,
            'tags': tags,
        }
    )


def post_detail(request, year, month, day, post):
    # Retrieve the post based on the provided year, month, day, and slug
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'similar_posts': similar_posts,
        },
    )


def post_search(request):
    form = SearchForm()
    query = None
    results = Post.published.none()
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(search=SearchVector('title', 'body')).filter(search=query)
    
    # Paginate the posts list, using the value from settings
    posts_per_page = getattr(settings, 'POSTS_PER_PAGE', 3)  # Default to 6 if setting is not defined
    paginator = Paginator(results, posts_per_page)
    page_number = request.GET.get('page', 1)
    tags = Tag.objects.all()  # Get all tags

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range, get last page of results
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {
            'posts': posts,
            'query': query,
            'form': form,
            'tags': tags,
        }
    )


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']],
            )
            sent = True
    else:
        form = EmailPostForm()
    
    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        },
    )