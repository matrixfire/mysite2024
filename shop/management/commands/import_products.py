import csv
import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from shop.models import Category, Collection, Product, ProductImage
import time, random


class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                time.sleep(random.randint(1, 3))
                if row['name']:
                    category, created = Category.objects.get_or_create(
                        name=row['category'],
                        slug=slugify(row['category'])
                    )
                    collection, created = Collection.objects.get_or_create(
                        name=row['collection'],
                        slug=slugify(row['collection'])
                    )
                    product, created = Product.objects.get_or_create(
                        category=category,
                        name=row['name'],
                        slug=row['slug'],
                        defaults={
                            'short_description': row['short_description'],
                            'description': row['description'],
                            'price': self.parse_price(row['price']),
                            'available': self.parse_boolean(row['available']),
                            'handle': row['handle'],
                        }
                    )
                    product.collections.add(collection)

                    if row['image']:
                        self.download_and_save_image(product, row['image'])

                    self.stdout.write(self.style.SUCCESS(f'Successfully imported product: {row["name"]}'))
                else:
                    product = Product.objects.get(handle=row['handle'])
                    product_image, created = ProductImage.objects.get_or_create(
                        product=product,
                        handle=row['handle'],
                        defaults={'image': self.download_image(row['image'])}
                    )
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported product image for handle: {row["handle"]}'))

    def download_and_save_image(self, product, image_url):
        """Download an image from a URL and save it to the product's image field."""
        image_file = self.download_image(image_url)
        if image_file:
            product.image.save(os.path.basename(image_url), image_file, save=True)

    def download_image(self, image_url):
        """Download an image from a URL and return a ContentFile."""
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for request errors
            return ContentFile(response.content)
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error downloading image from {image_url}: {e}'))
            return None

    def parse_price(self, price):
        """Convert price string to a Decimal, handling empty values."""
        if price:
            try:
                return float(price)
            except ValueError:
                self.stdout.write(self.style.WARNING(f'Invalid price value: {price}'))
        return 0  # Always 0 as per requirement

    def parse_boolean(self, value):
        """Convert string to boolean, handling various true/false representations."""
        return value.strip().lower() in ['true', '1', 't', 'y', 'yes']

# Example usage:
# python manage.py import_products path/to/your/input.csv
