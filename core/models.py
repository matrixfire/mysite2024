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
