# Generated by Django 5.0 on 2024-01-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0013_experience_job_role_experience_responsibilities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='job_role',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
