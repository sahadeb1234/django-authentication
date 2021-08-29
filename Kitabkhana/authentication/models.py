from django.db import models

# Create your models here.

class SliderImage(models.Model):
    image = models.ImageField(upload_to="slider/")