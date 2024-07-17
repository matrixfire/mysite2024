from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify
from .models import Post
from django.utils.text import slugify
from .models import Post

def duplicate_post(modeladmin, request, queryset):
    for post in queryset:
        new_post = post
        new_post.pk = None  # This will create a new instance
        new_post.title = f"{post.title} (Copy)"
        
        # Generate a unique slug
        original_slug = slugify(new_post.title)
        new_slug = original_slug
        counter = 1
        while Post.objects.filter(slug=new_slug).exists():
            new_slug = f"{original_slug}-{counter}"
            counter += 1
        new_post.slug = new_slug
        
        new_post.save()
        
duplicate_post.short_description = "Duplicate selected posts"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    actions = [duplicate_post]


admin.site.register(Post, PostAdmin)
