# Generated by Django 3.2.7 on 2021-09-17 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_customershasaddresses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='customers',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='reviewId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='products',
            new_name='product',
        ),
    ]
