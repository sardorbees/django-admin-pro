from django.db import models
from django.utils.text import slugify

class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='laptops/')
    img = models.ImageField(upload_to='laptops/')

    def __str__(self):
        return self.name
