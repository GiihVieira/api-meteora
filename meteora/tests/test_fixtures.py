from django.test import TestCase
from meteora.models import Product, Category
from decimal import Decimal


class FixturesTestCase(TestCase):
    
    fixtures = ['base_test.json']

    def test_carregamento_fixtures(self):
        '''Teste que verifica o carregamento da Fixtures'''
        product = Product.objects.get(name = 'Cadeira de Escritório Ergonômica')
        category = Category.objects.get(pk = 2)
        self.assertEqual(product.price, Decimal('699.90'))
        self.assertEqual(category.name, 'Móveis')

