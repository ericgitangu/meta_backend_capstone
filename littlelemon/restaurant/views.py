from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, MenuSerializer, BookingSerializer
from django.views import View
from django.shortcuts import render
from django.core import serializers
from .forms import BookingForm
import json
from django.views.generic import TemplateView
from datetime import datetime
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from .models import Menu, Booking
from .serializer import UserSerializer, MenuSerializer, BookingSerializer
from django.views import View
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
from .forms import BookingForm
import json
from datetime import datetime
from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    extra_actions = ['create', 'list', 'retrieve', 'update', 'destroy']


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['create', 'list', 'retrieve', 'update', 'destroy']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    extra_actions = ['create', 'list', 'update', 'destroy']
    permission_classes = [permissions.IsAuthenticated]


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutView(TemplateView):
    template_name = 'about.html'


class ReservationsView(View):
    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        bookings = Booking.objects.all()
        booking_json = serializers.serialize('json', bookings)
        return render(request, 'bookings.html', {"bookings": booking_json})


class BookView(View):
    def get(self, request):
        form = BookingForm()
        context = {'form': form}
        return render(request, 'book.html', context)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, 'book.html', context)


class MenuView(View):
    def get(self, request):
        menu_data = Menu.objects.all()
        main_data = {"menu": menu_data}
        return render(request, 'menu.html', {"menu": main_data})


class MenuItemView(View):
    def get(self, request, pk=None):
        if pk:
            menu_item = Menu.objects.get(pk=pk)
        else:
            menu_item = ""
        return render(request, 'menu_item.html', {"menu_item": menu_item})


class BookingsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
                reservation_slot=data['reservation_slot']).exists()
            if not exist:
                booking = Booking(
                    name=data['name'],
                    reservation_date=data['reservation_date'],
                    reservation_slot=data['reservation_slot'],
                )
                booking.save()
            else:
                return JsonResponse({'error': 1})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def get(self, request):
        try:
            date = request.GET.get('date', datetime.today().date())

            bookings = Booking.objects.all().filter(reservation_date=date)
            booking_json = serializers.serialize('json', bookings)

            return JsonResponse(booking_json, content_type='application/json')
        except Exception as e:
            return JsonResponse({'error': str(e)})
