from rest_framework import serializers
from meteora.models import Category, Product, Image
from meteora.validators import price_validation, stock_validation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = '__all__'

    def validate(self, data):
        if price_validation(data['price']):
            raise serializers.ValidationError({'price' : 'needs to be positive'})
        if stock_validation(data['qtd_stock']):
            raise serializers.ValidationError({'qtd_stock' : 'needs to be positive'})
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Image
        fields = '__all__'
