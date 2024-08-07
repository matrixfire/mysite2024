from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name




class PublishedManager(models.Manager):
    def get_queryset(self):
        # Returns only the posts that have a status of 'PUBLISHED'
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        # Different statuses for a post
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)  # Title of the post
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # Unique slug for the post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    author_image = models.ImageField(upload_to='authors/', blank=True, null=True)  # Optional author image
    # body = models.TextField()  # Content of the post
    body = RichTextUploadingField()  # Changed to CKEditor rich text uploading field
    publish = models.DateTimeField(default=timezone.now)  # Publish date of the post
    created = models.DateTimeField(auto_now_add=True)  # Auto set the field to now when the object is created
    updated = models.DateTimeField(auto_now=True)  # Auto set the field to now when the object is saved
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)  # Status of the post
    tags = TaggableManager(blank=True)  # Made tags optional
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)  # Made categories optional
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)


    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Custom manager to handle published posts
    

    class Meta:
        ordering = ['-updated', '-publish']  # Order posts by publish date descending
        indexes = [models.Index(fields=['-publish'])]  # Index on the publish date for faster queries

    def __str__(self):
        return self.title  # String representation of the post

    def get_absolute_url(self):
        # Return the URL to the post detail page
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def get_embed_url(self):
        # Return the embed URL for a video post
        if self.post_type == self.PostType.VIDEO:
            from urllib.parse import urlparse, parse_qs
            url_data = urlparse(self.video_url)
            query = parse_qs(url_data.query)
            video_id = query["v"][0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    def save(self, *args, **kwargs):
        # Ensure the slug is set before saving
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
