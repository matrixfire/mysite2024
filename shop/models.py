from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Category(models.Model):
    # Represents a category of products
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/', blank=True)

    class Meta:
        ordering = ['name']  # Order categories by name
        indexes = [models.Index(fields=['name'])]  # Index on the name field
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Returns the URL to access a particular category instance
        return reverse('shop:product_list_by_category', args=[self.slug])


class Collection(models.Model):
    # Represents a collection of products
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)  # unique implies the creation of an index

    class Meta:
        ordering = ['name']  # Order collections by name
        indexes = [models.Index(fields=['name'])]  # Index on the name field
        verbose_name = 'collection'
        verbose_name_plural = 'collections'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Returns the URL to access a particular collection instance
        return reverse('shop:product_list_by_collection', args=[self.slug])


class Product(models.Model):
    # Represents a product
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    collections = models.ManyToManyField(Collection, related_name='products', blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    short_description = models.TextField(blank=True)
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    sku = models.CharField(max_length=50, unique=True)
    handle = models.CharField(max_length=200, unique=True, default='default-handle')  # New field

    class Meta:
        ordering = ['name']  # Order products by name
        indexes = [
            models.Index(fields=['id', 'slug']),  # Composite index on id and slug
            models.Index(fields=['name']),  # Index on the name field
            models.Index(fields=['-created']),  # Index on the created field, in descending order
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Returns the URL to access a particular product instance
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductImage(models.Model):
    # Represents an image for a product
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)
    handle = models.CharField(max_length=200)  # New field


