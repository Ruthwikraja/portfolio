# Generated by Django 5.0 on 2024-01-05 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0025_portfolio_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='image',
        ),
    ]
