# Generated by Django 5.0.7 on 2024-07-31 09:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='written',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]