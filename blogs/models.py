from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    education = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/blogs/')
    auther_id = models.ManyToManyField(Author, related_name='blogs')

    def __str__(self):
        return self.title
