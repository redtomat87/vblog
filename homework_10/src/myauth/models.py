from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class VblogUser(AbstractUser):
    # date_joined = None
    # email = models.EmailField('email address', unique=True)
    bio = models.TextField('biography', blank=True)
