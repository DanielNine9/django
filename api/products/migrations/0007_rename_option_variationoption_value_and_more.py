# Generated by Django 5.0.3 on 2024-03-10 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rename_value_variationoption_option_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variationoption',
            old_name='option',
            new_name='value',
        ),
        migrations.AlterUniqueTogether(
            name='variationoption',
            unique_together={('value', 'variation_name')},
        ),
    ]
