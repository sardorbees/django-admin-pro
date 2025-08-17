# models.py
from django.db import models

class ProcessStep(models.Model):
    title = models.CharField(max_length=255)
    mini_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
