from django.contrib import admin

from .models import Post





class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['classic_image'].required = False
        form.base_fields['video_url'].required = False
        form.base_fields['carousel_image1'].required = False
        form.base_fields['carousel_image2'].required = False
        form.base_fields['carousel_image3'].required = False

        if obj:
            if obj.post_type == Post.PostType.CLASSIC_IMAGE:
                form.base_fields['classic_image'].required = True
            elif obj.post_type == Post.PostType.VIDEO:
                form.base_fields['video_url'].required = True
            elif obj.post_type == Post.PostType.CAROUSEL:
                form.base_fields['carousel_image1'].required = True

        return form


admin.site.register(Post, PostAdmin)
