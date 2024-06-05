from django.contrib import admin
from .models import Slide


# Register your models here.
# admin.site.register(Slide)
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['img', 'title', 'subtitle']
    prepopulated_fields = {'subtitle': ('title',)}
    list_editable = ['title', 'subtitle']
    