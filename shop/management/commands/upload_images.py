import csv
import os
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from shop.models import Product, ProductImage

class Command(BaseCommand):
    help = 'Upload images to specific products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    product = Product.objects.get(handle=row['handle'])
                    if row['image']:
                        img_url = row['image'].split("?")[0]
                        image_file = self.download_image(img_url)
                        if image_file:
                            ProductImage.objects.create(
                                product=product,
                                image=image_file,
                                handle=row['handle']
                            )
                            self.stdout.write(self.style.SUCCESS(f'Successfully uploaded image for product handle: {row["handle"]}'))
                        else:
                            self.stdout.write(self.style.ERROR(f'Failed to download image for product handle: {row["handle"]}'))
                    else:
                        self.stdout.write(self.style.ERROR(f'No image URL provided for product handle: {row["handle"]}'))
                except Product.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Product with handle {row["handle"]} does not exist'))

    def download_image(self, image_url):
        """Download an image from a URL and return a ContentFile."""
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for request errors
            return ContentFile(response.content, os.path.basename(image_url))
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error downloading image from {image_url}: {e}'))
            return None

# Example usage:
# python manage.py upload_images path/to/your/input.csv
# python manage.py upload_images product_imgs.csv