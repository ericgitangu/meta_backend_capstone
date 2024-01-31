from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, MenuSerializer, BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    extra_actions = ['create','list', 'retrieve', 'update', 'destroy']

class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    extra_actions = ['create', 'list']


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['create', 'list', 'retrieve', 'update', 'destroy']

class SingleMenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['list', 'retrieve', 'update', 'destroy']

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    extra_actions = ['create', 'list', 'update', 'destroy']
    permission_classes = [permissions.IsAuthenticated]

