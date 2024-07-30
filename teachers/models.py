from django.db import models


class Teacher(models.Model):
    class RatingChoices(models.TextChoices):
        Beginner = 'Beginner',
        Junior = 'Junior',
        Middle = 'Middle ',
        Senior = 'Senior',
        Expert = 'Expert'

    full_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Junior.value)
    twitter_link = models.CharField(max_length=150, null=True, blank=True)
    facebook_link = models.CharField(max_length=150, null=True, blank=True)
    linkedin_link = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)

    def __str__(self):
        return self.full_name
