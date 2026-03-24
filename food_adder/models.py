from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=255)
    