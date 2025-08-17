# products/serializers.py
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        ref_name = 'SlujhghjfhfhdfghfghdfghgText'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        ref_name = 'SlujhghjfghgText'

from rest_framework import serializers
from .models import Power

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ['id', 'name', 'slug']
        ref_name = 'rtyrtyrt'

from rest_framework import serializers
from .models import ProductType

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'slug']
        ref_name = 'aasfeir9uorehuhwugbwweyfb'


# shop_category/serializers.py

from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug']
        ref_name = 'sdasuhaurgandf'


from rest_framework import serializers
from .models import SolarPanel

class SolarPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarPanel
        fields = '__all__'
        ref_name = 'ger9hurgufbgufd'
