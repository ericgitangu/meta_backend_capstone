from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu, booking
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, MenuItemSerializer, BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['list']

class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['create']


class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    extra_actions = ['create', 'list']

class SingleMenuItemViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    extra_actions = ['retrieve', 'update', 'destroy']

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    extra_actions = ['create', 'list', 'update', 'destroy']

