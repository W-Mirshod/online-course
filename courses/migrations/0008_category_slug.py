# Generated by Django 5.0.7 on 2024-07-31 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_comment_written_alter_comment_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
