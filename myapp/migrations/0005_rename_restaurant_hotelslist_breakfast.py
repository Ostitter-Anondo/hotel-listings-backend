# Generated by Django 5.2.1 on 2025-05-16 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_hotelslist_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelslist',
            old_name='restaurant',
            new_name='breakfast',
        ),
    ]
