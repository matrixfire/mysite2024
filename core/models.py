from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile



class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)

    def __str__(self):
        return self.title



class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
class BusinessInfo(models.Model):
    brand_name = models.CharField(max_length=255)
    facebook_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    about_us = models.TextField(blank=True)
    # Add more fields as needed for your business information

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural = "Business Information"


class BusinessPost(models.Model):
    business_info = models.OneToOneField(BusinessInfo, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='business/', blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
