from django.contrib import admin
from .models import Slide, Subscriber, BusinessInfo, BusinessPost, HomepageContent


# Register your models here.
# admin.site.register(Slide)
# @admin.register(Slide)
# class SlideAdmin(admin.ModelAdmin):
#     list_display = ['img', 'title', 'subtitle']
#     # prepopulated_fields = {'subtitle': ('title',)}
#     list_editable = ['title', 'subtitle']
    
admin.site.register(Slide)
admin.site.register(Subscriber)


class BusinessPostInline(admin.StackedInline):
    model = BusinessPost
    can_delete = False
    extra = 0  # No extra forms

@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    inlines = [BusinessPostInline]
    list_display = ['brand_name', 'facebook_url', 'youtube_url', 'instagram_url', 'linkedin_url']
    search_fields = ['brand_name']

@admin.register(BusinessPost)
class BusinessPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'business_info']
    search_fields = ['title', 'business_info__brand_name']


@admin.register(HomepageContent)
class HomepageContentAdmin(admin.ModelAdmin):
    pass