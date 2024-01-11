# Generated by Django 5.0 on 2024-01-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0029_imagefile_is_primary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=155)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]