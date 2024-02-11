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
        """
        Creates a bearer token for the given username and password.

        Args:
            username (str): The username.
            password (str): The password.

        Returns:
            str: The bearer token key.
        """
        data = {
            'username': username,
            'password': password
        }
        serializer = TokenCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return token.key

    def setUp(self):
            """
            Set up the test environment for the getall endpoint.

            This method is called before each test case to initialize the necessary objects and variables.
            It creates three Menu objects with different titles, prices, and inventories.
            """
            print("\n---- 1. Test Setup for the getall endpoint----")
            self.client = APIClient()
            self.menu1 = Menu.objects.create(
                name='Menu 1', price=10.99, inventory=10)
            self.menu2 = Menu.objects.create(
                name='Menu 2', price=15.99, inventory=20)
            self.menu3 = Menu.objects.create(
                name='Menu 3', price=12.99, inventory=30)
            print('\tSetup complete ✅')

    def tearDown(self):
        """
        This method is called after each test case to clean up any resources used during the test.
        It deletes all Menu objects from the database and prints a message indicating the completion of teardown.
        """
        print("\n---- 1. Test Teardown----")
        Menu.objects.all().delete()
        print('\tTeardown complete for the *getall* endpoint ✅')

    def test_getall(self):
        """
        Test case for the `getall` endpoint.

        This test case verifies the behavior of the `getall` endpoint by making a GET request to the endpoint
        and asserting the response status code and data against the expected values.

        Steps:
        1. Generate a bearer token by making a POST request to the login endpoint.
        2. Set the authorization header with the bearer token.
        3. Make a GET request to the `menu-list` endpoint.
        4. Retrieve all the Menu objects from the database.
        5. Serialize the Menu objects.
        6. Assert the response status code is 200.
        7. Assert the response data matches the serialized data.
        """

        print("\n---- 1. Testing the *getall* endpoint----")
        url = reverse('menu-list')
        bearer_token = requests.post('http://127.0.0.1:8000/auth/token/login', data={
                                     'username': 'bistroadmin', 'password': 'lemon@786!'}).json()['auth_token']
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        }
        response = self.client.get(url, headers=headers)
        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data

        print('\n---- 1. Assert Status codes----')
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, msg="Status code is not 200")
        print('\tPassed Status Codes assertion ✅')

        print('\n---- 1. Assert Response Data----')
        self.assertEqual(response.data['results'], serialized_data)
        print('\tPassed Response Data assertion ✅')

        print('\n\tTest the *getall* endpoint successfully ✅')
