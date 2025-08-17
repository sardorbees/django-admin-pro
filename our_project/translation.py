from modeltranslation.translator import translator, TranslationOptions
from .models import Card

class CardTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')

translator.register(Card, CardTranslationOptions)
