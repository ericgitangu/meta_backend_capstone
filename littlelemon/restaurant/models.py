from django.db import models
from rest_framework import viewsets
from django.db import models
from rest_framework import viewsets

class User(viewsets.ViewSet):
    url = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    groups = models.ManyToManyField('api_auth.Group')

    def __str__(self) -> str:
        return super().__str__()

class Menu(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, default='')
    inventory = models.SmallIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['title', 'inventory', 'price']
        verbose_name_plural = 'Menu'

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    class Meta:
        ordering = ['date', 'time']
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f'{self.name} : {self.date} - {self.time}'