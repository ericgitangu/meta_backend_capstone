from django.contrib import admin
from .models import Menu, booking
from django.contrib.auth.models import User

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_filter = ['price']
    list_per_page = 10
    list_display = ['name', 'description', 'price']
    list_editable = ['price']
    list_display_links = ['name', 'description']
    ordering = ['name', 'description']

@admin.register(booking)
class bookingAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'email']
    list_filter = ['date', 'time']
    list_per_page = 10
    list_display = ['name', 'phone', 'email', 'date', 'time', 'party_size']
    list_editable = ['party_size']
    list_display_links = ['name', 'phone', 'email']
    ordering = ['date', 'time']