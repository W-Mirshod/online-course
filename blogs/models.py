from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    education = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/blogs')
    auther_id = models.ManyToManyField(Author, related_name='blogs')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.title)}-{i}"
                if not Blog.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
