from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Food(models.Model):
    name = models.CharField(max_length=255)
    featured_image = CloudinaryField('image', default='placeholder')
