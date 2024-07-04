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


class DIYNews(models.Model):
    title = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='diynews/covers/', blank=True, null=True)
    html_content = RichTextField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.cover_image:
            # Open the image using Pillow
            img = Image.open(self.cover_image)
            # Calculate the new height to maintain aspect ratio
            output_size = (270, 310)
            img.thumbnail(output_size, Image.ANTIALIAS)
            
            # Save the modified image
            img_io = BytesIO()
            img.save(img_io, format='JPEG', quality=85)
            img_content = ContentFile(img_io.getvalue(), self.cover_image.name)
            self.cover_image.save(self.cover_image.name, img_content, save=False)
            
        super().save(*args, **kwargs)

    def image_tag(self):
        if self.cover_image:
            return mark_safe(f'<img src="{self.cover_image.url}" width="270" height="310" />')
        return ""

    image_tag.short_description = 'Cover Image'




# class Carousel(models.Model):
#     # image       = models.ImageField(upload_to="pics/%y/%m/%d/")
#     image       = models.ImageField(upload_to="pics/")
#     title       = models.CharField(max_length=150)
#     action_name = models.CharField(max_length=50)
#     link        = models.TextField(null=True, blank=True)
#     sub_title   = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.title