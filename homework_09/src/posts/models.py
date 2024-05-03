from django.db import models
from datetime import datetime

from writers.models import Writer

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_at = models.DateField(default=datetime.now)

    author = models.OneToOneField(
        Writer,
#        primary_key=True,
        on_delete=models.CASCADE,
    ) 
    tags = models.ManyToManyField('Tags', related_name='tags')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Tags(models.Model):
    name = models.CharField(max_length=64)
#     post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name