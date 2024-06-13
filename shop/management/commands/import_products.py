import csv
import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from shop.models import Category, Collection, Product

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
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
                    }
                )
                product.collections.add(collection)

                if row['image']:
                    self.download_and_save_image(product, row['image'])

                self.stdout.write(self.style.SUCCESS(f'Successfully imported product: {row["name"]}'))

    def download_and_save_image(self, product, image_url):
        """Download an image from a URL and save it to the product's image field."""
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for request errors
            image_name = os.path.basename(image_url)
            product.image.save(image_name, ContentFile(response.content), save=True)
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error downloading image for {product.name}: {e}'))

    def parse_price(self, price):
        """Convert price string to a Decimal, handling empty values."""
        if price:
            try:
                return float(price)
            except ValueError:
                self.stdout.write(self.style.WARNING(f'Invalid price value: {price}'))
        return None

    def parse_boolean(self, value):
        """Convert string to boolean, handling various true/false representations."""
        return value.strip().lower() in ['true', '1', 't', 'y', 'yes']
