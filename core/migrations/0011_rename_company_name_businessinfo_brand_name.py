# Generated by Django 5.0.6 on 2024-07-08 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_businessinfo_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessinfo',
            old_name='company_name',
            new_name='brand_name',
        ),
    ]
