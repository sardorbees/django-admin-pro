# products/admin.py
from django.contrib import admin
from .models import Category, Product, Power

from django.contrib import admin
from .models import ProductType

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'price', 'old_price', 'installment_price',
        'color', 'brand', 'rating', 'reviews', 'in_stock', 'is_available', 'views', 'power'
    )
    list_filter = ('category', 'color', 'brand', 'in_stock', 'is_available', 'power')
    search_fields = ('name', 'description', 'color', 'brand')
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('views',)
    ordering = ('-id',)

from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'rating', 'price']
    prepopulated_fields = {'slug': ('name', 'rating', 'price')}
    search_fields = ['name', 'rating', 'price']

from django.contrib import admin
from .models import SolarPanel  # или SolarPanel, если так называется

@admin.register(SolarPanel)
class SolarPanelAdmin(admin.ModelAdmin):
    list_display = ('name', 'power', 'price')
    list_filter = ('power',)
    search_fields = ('name',)

