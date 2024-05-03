from django.db import models

# Create your models here.

class Writer(models.Model):

    name = models.CharField(max_length=32, null=False, unique=True)
    email = models.CharField(max_length=32, null=True, unique=False)
    username = models.CharField(max_length=32, null=True)
    age = models.PositiveIntegerField(null=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name    

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
