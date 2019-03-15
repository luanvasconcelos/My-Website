from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    date_used = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='image_input')
