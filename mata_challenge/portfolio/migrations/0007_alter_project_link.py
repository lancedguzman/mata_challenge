# Generated by Django 5.2.3 on 2025-07-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_remove_project_first_created_project_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, default='Not Yet Available', max_length=500),
        ),
    ]
