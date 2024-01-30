from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('create-user/', views.CreateUserViewSet.as_view(), name='create-user'),
    # path('user-list/', views.UserViewSet.as_view(), name='user-list'),
    # path('api-auth/', include('rest_framework.urls')),
    # path('menu/', views.MenusViewSet.as_view({'get': 'list'}), name='menu'),
    # path('menu/<int:pk>/', views.SingleMenuViewSet.as_view(), name='single-menu-item'),
    # path('tables/', views.BookingViewSet.as_view({'get:list'}), name='tables'),
    path('api-token-auth/', obtain_auth_token)
]
