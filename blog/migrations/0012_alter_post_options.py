# Generated by Django 5.0.6 on 2024-07-17 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated', '-publish']},
        ),
    ]
