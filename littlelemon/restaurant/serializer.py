from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the User model.
    """
    class Meta:
        model = User
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for the Menu model.
    """
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """
    class Meta:
        model = Booking
        fields = '__all__'
