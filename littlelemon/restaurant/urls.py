from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('book/', views.BookView.as_view(), name="book"),
    path('reservations/', views.ReservationsView.as_view(), name="reservations"),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu_item/<int:pk>/', views.MenuItemView.as_view(), name="menu_item"),
    # path('restaurant/booking/tables/', views.BookingsView.as_view(), name='bookings'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signout/', views.LogoutView.as_view(), name='signout'),
]
