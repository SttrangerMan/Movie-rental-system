# Generated by Django 5.0.6 on 2024-05-15 01:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_orders'),
        ('movies_orders', '0002_movies_order_delete_movies_orders'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies_order',
            new_name='MovieOrder',
        ),
    ]
