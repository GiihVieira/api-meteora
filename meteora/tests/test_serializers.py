from django.test import TestCase
from meteora.models import Product, Category, Image
from meteora.serializers import ProductSerializer, CategorySerializer, ImageSerializer


class ProductSerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name        = 'Eletrônicos',
            description = 'Equipamentos Eletrônicos',
            make_in     = None,
            update_in   = None,
        )
        self.product = Product.objects.create(
            name        = 'Fone de Ouvido',
            description = 'Fone QCY H3 com ANC',
            price       = '350.00',
            qtd_stock   = '83',
            category    = self.category,
            image       = None,
            make_in     = None,
            update_in   = None,
        )
        self.product_serializer = ProductSerializer(instance = self.product)

    def test_product_fields_serializer(self):
        data = self.product_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'price', 'qtd_stock', 'category', 'image', 'make_in', 'update_in']))

    def test_product_fields_content_serializer(self):
        data = self.product_serializer.data
        self.assertEqual(data['name'], self.product.name)
        self.assertEqual(data['description'], self.product.description)
        self.assertEqual(data['price'], self.product.price)
        self.assertEqual(data['qtd_stock'], self.product.qtd_stock)
        self.assertEqual(data['category'], self.product.category.id)
        self.assertEqual(data['image'], self.product.image)
        self.assertEqual(data['make_in'], data['make_in'])
        self.assertEqual(data['update_in'], data['update_in'])


class CategorySerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name        = 'Informática',
            description = 'Tudo em equipamentos de T.I',
            make_in     = None,
            update_in   = None
        )
        self.category_serializer = CategorySerializer(instance = self.category)

    def test_category_fields_serializer(self):
        data = self.category_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'make_in', 'update_in']))

    def test_category_fields_content_serializer(self):
        data = self.category_serializer.data
        self.assertEqual(data['name'], self.category.name)
        self.assertEqual(data['description'], self.category.description)
        self.assertEqual(data['make_in'], data['make_in'])
        self.assertEqual(data['update_in'], data['update_in'])
        

class ImageSerializerTestCase(TestCase):
    def setUp(self):
        self.image = Image.objects.create(
            description = 'Test de criação de uma imagem',
            image       = None
        )
        self.image_serializer = ImageSerializer(instance = self.image)

    def test_image_fields_serializer(self):
        data = self.image_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'description', 'image']))

    def test_image_fields_content_serializer(self):
        data = self.image_serializer.data
        self.assertEqual(data['description'], self.image.description)
        self.assertEqual(data['image'], None)
