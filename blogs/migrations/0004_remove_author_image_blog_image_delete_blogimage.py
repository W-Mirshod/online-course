# Generated by Django 5.0.7 on 2024-07-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blog_auther_id_blog_auther_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='images/blogs/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
    ]