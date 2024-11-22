from django.test import TestCase
from meteora.models import Product, Category, Image


class ModelProductTestCase(TestCase):
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

    def test_product_attributes(self):
        self.assertEqual(self.product.name, 'Fone de Ouvido')
        self.assertEqual(self.product.description, 'Fone QCY H3 com ANC')
        self.assertEqual(self.product.price, '350.00')
        self.assertEqual(self.product.qtd_stock, '83')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.image, None)
        self.assertEqual(self.product.make_in, self.product.make_in)
        self.assertEqual(self.product.update_in, self.product.update_in)


class ModelCategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name        = 'Informática',
            description = 'Tudo em equipamentos de T.I',
            make_in     = None,
            update_in   = None
        )

    def test_category_attributes(self):
        self.assertEqual(self.category.name, 'Informática')
        self.assertEqual(self.category.description, 'Tudo em equipamentos de T.I')
        self.assertEqual(self.category.make_in, self.category.make_in)
        self.assertEqual(self.category.update_in, self.category.update_in)


class ModelImageTestCase(TestCase):
    def  setUp(self):
        self.image = Image.objects.create(
            description = 'Test de criação de uma imagem',
            image       = None
        )

    def test_image_attributes(self):
        self.assertEqual(self.image.description, 'Test de criação de uma imagem')
        self.assertEqual(self.image.image, None)
