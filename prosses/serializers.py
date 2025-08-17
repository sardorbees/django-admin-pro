# serializers.py
from rest_framework import serializers
from .models import ProcessStep

class ProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = '__all__'
