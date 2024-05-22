from django.db import models
from datetime import datetime
from django_prose_editor.fields import ProseEditorField

from writers.models import Writer

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = ProseEditorField()
    published_at = models.DateTimeField(default=datetime.now)

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

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()  # Поле для хранения ссылки на изображение
    image = models.ImageField(upload_to='images/', null=True, max_length=255)

    def __str__(self):
        return f"Image for {self.post.title}"
    def __repr__(self):
        return 'Resume(%s, %s)' % (self.post, self.file)    