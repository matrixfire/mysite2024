from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )



class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    class PostType(models.TextChoices):
        CLASSIC_IMAGE = 'CI', 'Classic with Image'
        CLASSIC_NO_IMAGE = 'CN', 'Classic without Image'
        VIDEO = 'VI', 'Video'
        CAROUSEL = 'CA', 'Carousel'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    author_image = models.ImageField(upload_to='authors/', blank=True, null=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)
    post_type = models.CharField(max_length=2, choices=PostType.choices, default=PostType.CLASSIC_NO_IMAGE)

    classic_image = models.ImageField(upload_to='posts/classic_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    carousel_image1 = models.ImageField(upload_to='posts/carousel_images/', blank=True, null=True)
    carousel_image2 = models.ImageField(upload_to='posts/carousel_images/', blank=True, null=True)
    carousel_image3 = models.ImageField(upload_to='posts/carousel_images/', blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def get_embed_url(self):
        if self.post_type == self.PostType.VIDEO:
            from urllib.parse import urlparse, parse_qs
            url_data = urlparse(self.video_url)
            query = parse_qs(url_data.query)
            video_id = query["v"][0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
















