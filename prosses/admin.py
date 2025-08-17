# admin.py
from django.contrib import admin
from .models import ProcessStep

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'mini_description']
