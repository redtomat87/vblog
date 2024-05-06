from django.db import models
from datetime import datetime

from writers.models import Writer

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_at = models.DateField(default=datetime.now)

    author = models.ForeignKey(
        Writer,
        on_delete=models.CASCADE,
    ) 

    tags = models.ManyToManyField(Tags)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'