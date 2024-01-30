from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'price']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ['name', 'phone', 'email', 'date', 'time', 'party_size']
