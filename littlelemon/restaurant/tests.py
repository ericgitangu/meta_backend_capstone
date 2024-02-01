from django.test import TestCase

from .models import Menu, Booking
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .serializer import MenuSerializer

from .models import Menu
import json
from djoser.serializers import TokenCreateSerializer
from rest_framework.authtoken.models import Token
import requests

class MenuViewTest(TestCase):
    """
    Test case for the MenuView class.

    This test case includes setup and teardown methods, as well as a test method for the `getall` endpoint.
    """

    def create_bearer_token(username, password):
        data = {
            'username': username,
            'password': password
        }
        serializer = TokenCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return token.key

    def setUp(self):
        print("\n----Test Setup for the getall endpoint----")
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Menu 1', price=10.99, inventory=10)
        self.menu2 = Menu.objects.create(title='Menu 2', price=15.99, inventory=20)
        self.menu3 = Menu.objects.create(title='Menu 3', price=12.99, inventory=30)
        print('\tSetup complete ✅')

    def tearDown(self):
        print("----Test Teardown----")
        Menu.objects.all().delete()
        print('\tTeardown complete ✅')

    def test_getall(self):
        url = reverse('menu-list')
        bearer_token = requests.post('http://127.0.0.1:8000/auth/token/login', data={'username': 'bistroadmin', 'password': 'lemon@786!'}).json()['auth_token']
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        }
        response = self.client.get(url, headers=headers)
        menus = Menu.objects.all()
        # print(menus)
        serialized_data = MenuSerializer(menus, many=True).data
        print('----Assert Status codes----')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Status code is not 200")
        print('\tPassed Status Codes assertion ✅')
        # print(response.data['results'])
        print('----Assert Response Data----')
        self.assertEqual(response.data['results'], serialized_data)
        print('\tPassed Response Data assertion ✅')

