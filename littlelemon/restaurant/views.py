from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, MenuSerializer, BookingSerializer
from django.views import View
from django.shortcuts import render, redirect
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
from .models import Booking
from .forms import BookingForm
import json
from datetime import datetime
from django.http import JsonResponse, HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import redirect
import requests
from django.contrib.auth import logout
import requests
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_protect


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['create']


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_actions = ['list']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    extra_actions = ['create', 'list', 'update', 'destroy']
    permission_classes = [permissions.IsAuthenticated]
    
class ProfileView(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        user = request.user
        profile = User.objects.get(username=user.username)
        return render(request, 'book.html')
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
        if request.user.is_authenticated:
            form = BookingForm()
            context = {'form': form}
            return render(request, 'book.html', context)
        else:
            base_url = request.build_absolute_uri('/')  # Get the base URL
            login_url = f"{base_url}restaurant/accounts/login"  # Construct the login URL
            return redirect(login_url)  # Redirect to the login URL

    def post(self, request):
        if request.user.is_authenticated:
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
            context = {'form': form}
            return render(request, 'book.html', context)
        else:
            return render(request=request, template_name='login.html')


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
    class BookingsView(View):
        @csrf_protect
        def post(self, request):
            if request.user.is_authenticated:
                print('User is authenticated!')
                try:
                    data = json.loads(request.body)
                    exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
                        reservation_slot=data['reservation_slot']).exists()
                    if not exist:
                        # booking = Booking(
                        #     name=data['name'],
                        #     phone=data['phone'],
                        #     email=data['email'],
                        #     reservation_date=data['reservation_date'],
                        #     reservation_slot=data['reservation_slot'],
                            
                        # )
                        # # booking.save()
                        
                        base_url = request.build_absolute_uri('/')  # Get the base URL
                        url = f"{base_url}restaurant/booking/tables/"  # Replace with the actual URL


                        data = {
                            "name": data['name'],
                            "phone": data['phone'],
                            "email": data['email'],
                            "reservation_date": data['reservation_date'],
                            "reservation_slot": data['reservation_slot'],
                        }
                        
                        try:
                            response = requests.post(url, data=json.dumps(data), headers={
                                                     'Content-Type': 'multipart/form-data', 'Authorization': f'Token {request.user.auth_token}', 'Accept': 'application/json'})
                            if response.status_code == 200:
                                print("Booking created successfully!")
                            else:
                                JsonResponse("Failed to create booking. Status code:", response.status_code)
                        except requests.exceptions.RequestException as e:
                            print("Error:", e)
                            return JsonResponse({'error': str(e)})
                    else:
                        print("Booking already exists!")
                        return JsonResponse({'error': 1})
                except Exception as e:
                    print("Error: ", e)
                    return JsonResponse({'error': str(e)})
            else:
                print("User not authenticated!")
                return redirect('/login')

        def get(self, request):
            print(request.body)
            try:
                date = request.GET.get('date', datetime.today().date())
                bookings = Booking.objects.all().filter(reservation_date=date)
                booking_json = serializers.serialize('json', bookings)

                return JsonResponse(booking_json, content_type='application/json')
            except Exception as e:
               print(e)
               return JsonResponse({'error': str(e)})

class LoginView(View):
    def get(self, request):
        url = "/restaurant/accounts/login"  # Replace with the actual URL
        response = requests.get(url)
        print(request.path)
        if response.status_code == 200:
            render(request, 'book.html')

    def post(self, request):
        pass

class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')
