# Generated by Django 5.0 on 2024-01-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0024_remove_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.FileField(null=True, upload_to='portfolio/'),
        ),
    ]
