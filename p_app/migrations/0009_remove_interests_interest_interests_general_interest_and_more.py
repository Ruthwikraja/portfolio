# Generated by Django 5.0 on 2024-01-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_app', '0008_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interests',
            name='interest',
        ),
        migrations.AddField(
            model_name='interests',
            name='General_interest',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='interests',
            name='Technical_interest',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
