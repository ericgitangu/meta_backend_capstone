from django.contrib import admin
from .models import Menu, Booking
from django.contrib.auth.models import User

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Admin class for managing the Menu model in the Django admin interface.
    """
    search_fields = ['title', 'price']
    list_filter = ['price']
    list_per_page = 10
    list_display = ['title', 'inventory', 'price']
    list_editable = ['price']
    list_display_links = ['title', 'inventory']
    ordering = ['title', 'inventory']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.
    
    This class defines the display, search, and filtering options for the Booking model in the Django admin interface.
    """
    search_fields = ['name', 'phone', 'email']
    list_filter = ['reservation_date', 'reservation_slot']
    list_per_page = 10
    list_display = ['name', 'phone', 'email', 'reservation_date', 'reservation_slot']
    list_editable = ['reservation_date', 'reservation_slot']
    list_display_links = ['name', 'phone', 'email']
    ordering = ['reservation_date', 'reservation_slot']