# laptops/serializers.py
from rest_framework import serializers
from .models import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'icon', 'img']
        ref_name = 'produysdguysdijmfh'