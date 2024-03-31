from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=32, null=False, unique=True)
    email = models.CharField(max_length=32, null=True, unique=False)
    username = models.CharField(max_length=32, null=True)
    age = models.PositiveIntegerField(null=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'