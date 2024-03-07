# Generated by Django 5.0.2 on 2024-03-07 04:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50, unique=True, verbose_name='active token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('expires_at', models.DateTimeField(verbose_name='expires at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='active_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]