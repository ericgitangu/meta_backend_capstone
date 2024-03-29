from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('book/', views.BookView.as_view(), name="book"),
    path('bookings/<int:pk>', views.BookingItemView.as_view(), name="booking-item"),
    path('reservations/', views.ReservationsView.as_view(), name="reservations"),
    path('reservations/<int:pk>/',
         views.ReservationsItemView.as_view(), name="reservation-item"),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu_item/<int:pk>/', views.MenuItemView.as_view(), name="menu_item"),
    # path('restaurant/booking/tables/', views.BookingsView.as_view(), name='bookings'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signout/', views.LogoutView.as_view(), name='signout'),
]

"""
URL patterns for the restaurant app.

This module defines the URL patterns for the restaurant app. It includes paths for the home, about, book, reservations, menu, menu_item, login, and signout views.

Author: Eric Gitangu
Date: Feb, 1st 2024
"""
