# Generated by Django 5.2.1 on 2025-05-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_hotelslist_pool_hotelslist_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelslist',
            name='rating',
            field=models.FloatField(),
        ),
    ]
