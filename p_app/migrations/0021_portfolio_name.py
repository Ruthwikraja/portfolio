# Generated by Django 5.0 on 2024-01-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0020_portfolio_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
