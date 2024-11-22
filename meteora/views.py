from rest_framework import viewsets, filters
from meteora.serializers import ProductSerializer, CategorySerializer, ImageSerializer
from meteora.models import Product, Category, Image
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset         = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends  = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]   
    ordering_fields  = ['name']
    search_fields    = ['name', 'category']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset         = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset         = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer
