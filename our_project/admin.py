from django.contrib import admin
from . import translation

from modeltranslation.admin import TranslationAdmin
from .models import Card

@admin.register(Card)
class CardAdmin(TranslationAdmin):
    list_display = ('title', 'desc')
#