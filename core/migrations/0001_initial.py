# Generated by Django 5.0.6 on 2024-05-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='slides/')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=300)),
            ],
        ),
    ]
