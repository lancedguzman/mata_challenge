# Generated by Django 5.2.3 on 2025-07-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='first_created',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='tech_stack',
            field=models.TextField(blank=True, default='', max_length=255),
        ),
    ]
