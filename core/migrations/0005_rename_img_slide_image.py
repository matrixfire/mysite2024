# Generated by Django 5.0.6 on 2024-07-03 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_carousel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='img',
            new_name='image',
        ),
    ]
