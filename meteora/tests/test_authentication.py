from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username = 'admin',
            password = 'admin'
        )
        self.url = reverse('Products-list')

    def test_authentication_user_with_correct_credentials(self):
        user = authenticate(
            username = 'admin',
            password = 'admin'
        )
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_authentication_user_with_incorrect_username(self):
        user = authenticate(
            username = 'amin',
            password = 'admin'
        )
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_user_with_incorrect_password(self):
        user = authenticate(
            username = 'admin',
            password = 'amin'
        )
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_user_request_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_request_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
