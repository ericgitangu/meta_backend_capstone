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
from django.shortcuts import redirect
import requests
from django.contrib.auth import logout
import requests
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_protect
from rest_framework import filters, pagination
from rest_framework.pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing user data.

    This viewset provides CRUD operations for the User model.
    It allows creating, reading, updating, and deleting user instances.

    Attributes:
        queryset (QuerySet): The queryset of User objects.
        serializer_class (Serializer): The serializer class for User objects.
        permission_classes (list): The list of permission classes for the viewset.
        extra_actions (list): The list of extra actions supported by the viewset.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    extra_actions = ['create']
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']
    # pagination_class = pagination.PageNumberPagination,
    paginate_by = 10

class MenuViewSet(viewsets.ModelViewSet):
    """
        A viewset for handling CRUD operations on Menu objects.

        Inherits from viewsets.ModelViewSet and provides default
        implementations for list, create, retrieve, update, and destroy actions.

        Attributes:
            queryset (QuerySet): The queryset of Menu objects.
            serializer_class (Serializer): The serializer class for Menu objects.
            permission_classes (list): The list of permission classes for the viewset.
            extra_actions (list): The list of extra actions supported by the viewset.
            filter_backends (list): The list of filter backends for the viewset.
            filterset_fields (list): The list of fields to filter on.
            search_fields (list): The list of fields to search on.
            ordering_fields (list): The list of fields to order on.
            pagination_class (Pagination): The pagination class for the viewset.
        """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    extra_actions = ['list']
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']
    # pagination_class = pagination.PageNumberPagination,
    paginate_by = 2

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on Booking objects.

    Inherits from viewsets.ModelViewSet, which provides default implementations
    for the standard list, create, retrieve, update, and destroy actions.

    Attributes:
        queryset (QuerySet): The queryset of Booking objects to be used by the viewset.
        serializer_class (Serializer): The serializer class to be used for serializing and deserializing Booking objects.
        extra_actions (list): A list of additional actions supported by the viewset.
        permission_classes (list): A list of permission classes that the viewset requires for accessing its endpoints.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    extra_actions = ['create', 'list', 'update', 'destroy']
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']
    # pagination_class = pagination.PageNumberPagination,
    paginate_by = 10


class ProfileView(View):
    """
    View class for displaying user profile.

    Requires the user to be logged in.
    Retrieves the user's profile from the database and renders the 'profile.html' template.
    """

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        user = request.user
        profile = User.objects.get(username=user.username)
        return render(request, 'profile.html', {'profile': profile})


class HomeView(View):
    def get(self, request):
        """
        Renders the index.html template.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - The rendered index.html template.
        """
        
        return render(request, 'index.html')


class AboutView(TemplateView):
    """
    A view that renders the about page.

    Inherits from TemplateView and uses the 'about.html' template.
    """
    template_name = 'about.html'


class ReservationsView(View):
    """
    A view for handling reservations.

    Methods:
    - get: Retrieves the reservations for a specific date and renders them in a template.
    """

    def get(self, request):
        date = request.GET.get('date', datetime.today().date())
        bookings = BookingViewSet().get_queryset()
        booking_json = serializers.serialize('json', bookings)
        return render(request, 'bookings.html', {"bookings": booking_json})
    
class ReservationsItemView(View):
    """
    A view class for handling requests related to reservations.

    Methods:
    - get(request, pk=None): Handles GET requests for retrieving a specific reservation or all reservations.
    """
    def get(self, request, pk=None):
        """
        Handles GET requests for retrieving a specific reservation or all reservations.

        Args:
        - request: The HTTP request object.
        - pk (optional): The primary key of the reservation to retrieve.

        Returns:
        - If pk is provided, returns the reservation with the specified primary key.
        - If pk is not provided, returns all reservations.
        """
        bookings = BookingViewSet().get_queryset()
        if pk is not None:
            booking = bookings.get(pk=pk)
        else:
            booking = bookings.all()

        return render(request, 'booking_item.html', {"booking": booking})


class BookView(View):
    """
    View class for handling booking requests.

    Methods:
    - get: Handles GET requests for booking. If the user is authenticated, it renders the booking form.
            If the user is not authenticated, it redirects to the login page.
    - post: Handles POST requests for booking. If the user is authenticated and the form is valid,
            it saves the booking and renders the booking form. If the user is not authenticated,
            it renders the login page.
    """
    def get(self, request):
        if request.user.is_authenticated:
            form = BookingForm()
            context = {'form': form}
            return render(request, 'book.html', context)
        else:
            base_url = request.build_absolute_uri('/')  # Get the base URL
            # Construct the login URL
            login_url = f"{base_url}restaurant/accounts/login"
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
        
class BookingItemView(View):
    """
    A view class for handling requests related to bookings.

    Methods:
    - get(request, pk=None): Handles GET requests for retrieving a specific booking or all bookings.
    """

    def get(self, request, pk=None):
        """
        Handles GET requests for retrieving a specific booking or all bookings.

        Args:
        - request: The HTTP request object.
        - pk (optional): The primary key of the booking to retrieve.

        Returns:
        - If pk is provided, returns the booking with the specified primary key.
        - If pk is not provided, returns all bookings.
        """
        bookings = BookingViewSet().get_queryset()
        if pk:
            booking = bookings.get(pk=pk)
        else:
            booking = bookings.all()

        return render(request, 'booking_item.html', {"booking": booking})


class MenuView(View):
    """
    A view class that handles the rendering of the menu page.

    Methods:
    - get: Handles the GET request and renders the menu.html template with the menu data.
    """

    def get(self, request):
        menu_data = MenuViewSet().queryset.all()
        main_data = {"menu": menu_data}
        return render(request, 'menu.html', {"menu": main_data})


class MenuItemView(View):
    """
    A view class for handling requests related to menu items.

    Methods:
    - get(request, pk=None): Handles GET requests for retrieving a specific menu item or all menu items.
    """

    def get(self, request, pk=None):
        """
        Handles GET requests for retrieving a specific menu item or all menu items.

        Args:
        - request: The HTTP request object.
        - pk (optional): The primary key of the menu item to retrieve.

        Returns:
        - If pk is provided, returns the menu item with the specified primary key.
        - If pk is not provided, returns all menu items.
        """
        menu = MenuViewSet().get_queryset()
        if pk:
            menu_item = menu.get(pk=pk)
        else:
            menu_item = menu.all()

        return render(request, 'menu_item.html', {"menu_item": menu_item})


class BookingsView(View):
    '''
        This class handles the creation of bookings.
        The booking endpoint is being used in lieu of this module.
    '''
    pass
    # @csrf_protect
    # def post(self, request):
    #     if request.user.is_authenticated:
    #         print('User is authenticated!')
    #         try:
    #             data = json.loads(request.body)
    #             exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
    #                 reservation_slot=data['reservation_slot']).exists()
    #             if not exist:
    #                 # booking = Booking(
    #                 #     name=data['name'],
    #                 #     phone=data['phone'],
    #                 #     email=data['email'],
    #                 #     reservation_date=data['reservation_date'],
    #                 #     reservation_slot=data['reservation_slot'],

    #                 # )
    #                 # # booking.save()

    #                 base_url = request.build_absolute_uri(
    #                     '/')  # Get the base URL
    #                 # Replace with the actual URL
    #                 url = f"{base_url}restaurant/booking/tables/"

    #                 data = {
    #                     "name": data['name'],
    #                     "phone": data['phone'],
    #                     "email": data['email'],
    #                     "reservation_date": data['reservation_date'],
    #                     "reservation_slot": data['reservation_slot'],
    #                 }

    #                 try:
    #                     response = requests.post(url, data=json.dumps(data), headers={
    #                                              'Content-Type': 'multipart/form-data', 'Authorization': f'Token {request.user.auth_token}', 'Accept': 'application/json'})
    #                     if response.status_code == 200:
    #                         print("Booking created successfully!")
    #                     else:
    #                         JsonResponse(
    #                             "Failed to create booking. Status code:", response.status_code)
    #                 except requests.exceptions.RequestException as e:
    #                     print("Error:", e)
    #                     return JsonResponse({'error': str(e)})
    #             else:
    #                 print("Booking already exists!")
    #                 return JsonResponse({'error': 1})
    #         except Exception as e:
    #             print("Error: ", e)
    #             return JsonResponse({'error': str(e)})
    #         else:
    #             print("User not authenticated!")
    #             return redirect('/login')

    #     def get(self, request):
    #         print(request.body)
    #         try:
    #             date = request.GET.get('date', datetime.today().date())
    #             bookings = Booking.objects.all().filter(reservation_date=date)
    #             booking_json = serializers.serialize('json', bookings)

    #             return JsonResponse(booking_json, content_type='application/json')
    #         except Exception as e:
    #            print(e)
    #            return JsonResponse({'error': str(e)})


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
