from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    parent = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE, related_name='children',
        verbose_name="Родительская категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(unique=True, verbose_name="URL товара")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"


class Power(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    slug = models.SlugField(unique=True, verbose_name="URL товара")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мощность (W)"
        verbose_name_plural = "Мощности (W)"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(unique=True, verbose_name="URL товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена")
    old_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="Старая цена")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    brand = models.CharField(max_length=100, null=True, blank=True, verbose_name="brand")
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Рейтинг")
    reviews = models.IntegerField(default=0, verbose_name="новинка")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    installment_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена в рассрочку")
    is_available = models.BooleanField(default=True, verbose_name="Активен")
    views = models.IntegerField(default=0, verbose_name="Просмотры")
    popularity = models.IntegerField(default=0, verbose_name="Популярность")
    power = models.PositiveIntegerField(null=True, blank=True, verbose_name="Мощность (W)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"



from django.db import models

class Power(models.Model):
    name = models.CharField(max_length=100, verbose_name=("имя"))
    slug = models.SlugField(unique=True, verbose_name=("товар url"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("w сколько")
        verbose_name_plural = ("w сколько")

from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name=("имя"))
    slug = models.SlugField(unique=True, verbose_name=("товар url"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Товар описание")
        verbose_name_plural = ("Товар описание")

# shop_category/models.py

from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name=("имя"))
    slug = models.SlugField(unique=True, blank=True, verbose_name=("url товар"))
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=("цена"))
    rating = models.FloatField(default=0, verbose_name=("райтинг"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Бранд")
        verbose_name_plural = ("Бранд")

from django.db import models


class SolarPanel(models.Model):
    name = models.CharField(max_length=255, verbose_name=("имя"))
    power = models.IntegerField(verbose_name=("w сколько"))  # мощность в ваттах
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("цена"))
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=("старая цена"))
    image = models.ImageField(upload_to='panels/', verbose_name=("фото"))

    def __str__(self):
        return f"{self.name} - {self.power}W"

    class Meta:
        verbose_name = ("Категория_магазина")
        verbose_name_plural = ("Категория_магазина")