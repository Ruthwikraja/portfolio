# Generated by Django 5.0 on 2024-01-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0015_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]