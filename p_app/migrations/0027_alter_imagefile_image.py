# Generated by Django 5.0 on 2024-01-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0026_remove_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.FileField(upload_to='portfolio/'),
        ),
    ]
