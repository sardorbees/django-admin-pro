# laptops/admin.py
from django.contrib import admin
from .models import ProductCategory

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'img')
    prepopulated_fields = {"icon": ("name",)}
