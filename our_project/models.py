from django.db import models

class Card(models.Model):
    icon = models.ImageField(upload_to='icons/', blank=True, null=True, verbose_name="Иконка")
    img = models.ImageField(upload_to='images/', verbose_name="Фото")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    desc = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title
