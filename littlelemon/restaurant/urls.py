from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    # path('create-user/', views.CreateUserViewSet.as_view(), name='create-user'),
    # path('user-list/', views.UserViewSet.as_view(), name='user-list'),
    # path('api-auth/', include('rest_framework.urls')),
    path('menu-list/', views.MenuItemsViewSet.as_view({'get': 'list'}), name='menu-list'),
    # path('menu/<int:pk>/', views.SingleMenuItemViewSet.as_view(), name='single-menu-item'),
    # path('tables/', views.BookingViewSet.as_view({'get:list'}), name='tables'),
]
