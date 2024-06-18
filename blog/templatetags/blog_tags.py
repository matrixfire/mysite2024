import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from ..models import Post
from taggit.models import Tag

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5): # usage: {% get_most_commented_posts as most_commented_posts %}
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag('blog/sidebar.html', takes_context=True)
def show_sidebar(context, author=None):
    tags = Tag.objects.all()
    return {
        'request': context['request'],
        'author': author,
        'tags': tags,  # Add tags to the context
    }