# products/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Product, ProductType, Power
from shop_category.models import Brand, SolarPanel

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProductTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')

class PowerTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

class BrandTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

class SolarPanelTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)
translator.register(ProductType, ProductTypeTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Power, PowerTranslationOptions)
translator.register(SolarPanel, SolarPanelTranslationOptions)
