# Generated by Django 5.0.3 on 2024-03-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_product_variationname_variationoption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variationname',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
