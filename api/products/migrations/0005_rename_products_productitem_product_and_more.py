# Generated by Django 5.0.2 on 2024-03-04 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_created_date_product_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productitem',
            old_name='products',
            new_name='product',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'category')},
        ),
    ]
