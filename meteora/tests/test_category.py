from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from meteora.models import Category


class CategoryTestCase(APITestCase):

    fixtures = ['base_test.json']
    
    def setUp(self):
        self.user = User.objects.get(username = 'giovane')
        self.url = reverse('Categories-list')
        self.client.force_authenticate(self.user)
        self.category = Category.objects.get(pk = 2)

    def test_get_category(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_category(self):
        response = self.client.get(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_category(self):
        data = {
            'name'        : 'Test POST Category',
            'description' : 'Description POST Test Category'
        }
        response = self.client.post(self.url, data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_one_category(self):
        data = {
            'name'        : 'Test PUT Category',
            'description' : 'Description PUT Test Category'
        }
        response = self.client.put(f'{self.url}2/', data = data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_one_category(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
