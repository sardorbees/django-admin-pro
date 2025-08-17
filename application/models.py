from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=("полное имя"))
    phone = models.CharField(max_length=20, verbose_name=("телефон"))
    address = models.CharField(max_length=255, verbose_name=("адрес"))
    description = models.TextField(blank=True, verbose_name=("описание"))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=("IP-адрес"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("создано_at"))

    def __str__(self):
        return f"{self.full_name} — {self.phone}"
