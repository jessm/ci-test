# Generated by Django 4.1.1 on 2022-10-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['name'], name='backend_tag_name_194adf_idx'),
        ),
        migrations.AddIndex(
            model_name='taggroup',
            index=models.Index(fields=['name'], name='backend_tag_name_d4b9f9_idx'),
        ),
    ]
