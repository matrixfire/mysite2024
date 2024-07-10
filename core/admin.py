from django.contrib import admin
from .models import Slide, Subscriber, BusinessInfo, BusinessPost


# Register your models here.
# admin.site.register(Slide)
# @admin.register(Slide)
# class SlideAdmin(admin.ModelAdmin):
#     list_display = ['img', 'title', 'subtitle']
#     # prepopulated_fields = {'subtitle': ('title',)}
#     list_editable = ['title', 'subtitle']
    
admin.site.register(Slide)
admin.site.register(Subscriber)


class BusinessPostInline(admin.TabularInline):
    model = BusinessPost
    extra = 1  # Number of extra forms to display
    fields = ['title', 'image', 'body']  # Fields to display in the inline form


@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'facebook_url', 'youtube_url', 'instagram_url', 'linkedin_url']
    search_fields = ['brand_name']
    inlines = [BusinessPostInline]  # Include the inline


@admin.register(BusinessPost)
class BusinessPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'business_info', 'body']
    search_fields = ['title', 'business_info__brand_name']
    list_filter = ['business_info']
