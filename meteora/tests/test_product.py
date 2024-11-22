from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from meteora.models import Product, Category


class ProductTestCase(APITestCase):
    
    fixtures = ['base_test.json']
    
    def setUp(self):
        self.user = User.objects.get(username = 'giovane')
        self.url = reverse('Products-list')
        self.client.force_authenticate(user = self.user)
        self.product1 = Product.objects.get(pk = 1)
        self.category1 = Category.objects.get(pk = 1)

    def test_get_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_product(self):
        response = self.client.get(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_product(self):
        data = {
            'name' : 'Product Test',
            'description' : 'Product description test',
            'price' : 150.55,
            'qtd_stock' : 1000,
            'category' : self.category1.pk,
            'make_in' : '2024-11-21T15:25:19Z',
            'update_in' : '2024-11-21T15:25:19Z'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_one_product(self):
        data = {
                'name' : 'Product Test',
                'description' : 'Product description test',
                'price' : 150.55,
                'qtd_stock' : 1000,
                'category' : self.category1.pk,
                'make_in' : '2024-11-21T15:25:19Z',
                'update_in' : '2024-11-21T15:25:19Z'
        }
        response = self.client.put(f'{self.url}1/', data = data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_one_product(self):
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        