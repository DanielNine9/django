# Generated by Django 5.0.3 on 2024-03-10 10:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(blank=True, choices=[('B', 'billing'), ('S', 'shipping')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL),
        ),
    ]