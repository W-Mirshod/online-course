from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    education = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    auther_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(upload_to='images/')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
