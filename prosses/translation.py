# products/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import ProcessStep

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'mini_description', 'description')

translator.register(ProcessStep, CategoryTranslationOptions)
