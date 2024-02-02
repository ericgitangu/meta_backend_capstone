from django.db import models
from rest_framework import viewsets
from django.db import models
from rest_framework import viewsets

class User(viewsets.ViewSet):
    """
    Represents a user in the system.

    Attributes:
        url (str): The URL of the user.
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
        groups (ManyToManyField): The groups the user belongs to.
    """

    url = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 
    email = models.EmailField()
    groups = models.ManyToManyField('api_auth.Group', default='')

    def __str__(self) -> str:
        return super().__str__()

class Menu(models.Model):
    """
    Represents a menu item in the restaurant.

    Attributes:
        title (str): The title of the menu item.
        inventory (int): The number of items available in the inventory.
        price (Decimal): The price of the menu item.
        description (str): The description of the menu item (optional).

    Meta:
        ordering (list): The ordering of menu items in the database.
        verbose_name_plural (str): The plural name for the menu items.

    Methods:
        __str__(): Returns a string representation of the menu item.

    """

    title = models.CharField(max_length=255, null=False, blank=False, default='')
    inventory = models.SmallIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['title', 'inventory', 'price']
        verbose_name_plural = 'Menu'

    def __str__(self):
        return str(self.title) + ' : ' + str(self.price)

class Booking(models.Model):
    """
    Represents a booking made by a customer.

    Attributes:
        name (str): The name of the customer.
        phone (str): The phone number of the customer.
        email (str): The email address of the customer.
        reservation_date (date): The date of the reservation.
        reservation_slot (time): The time slot of the reservation.
    """

    name = models.CharField(max_length=255, null=False, blank=False, default='')
    phone = models.CharField(max_length=10, null=False, blank=False, default='')
    email = models.EmailField(null=False, blank=False, default='')
    reservation_date = models.DateField()
    reservation_slot = models.TimeField()

    class Meta:
        ordering = ['reservation_date', 'reservation_slot']
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.name} : {self.reservation_date} - {self.reservation_slot}'