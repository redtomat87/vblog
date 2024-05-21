from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Writer(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.username    

    class Meta:
        verbose_name = 'Writer'
        verbose_name_plural = 'Writers'


class WriterProfile(models.Model):
    # id = ...
    writer = models.OneToOneField(
        Writer,
        primary_key=True,
        on_delete=models.CASCADE,
    )  # writer_id
    biography = models.TextField()
