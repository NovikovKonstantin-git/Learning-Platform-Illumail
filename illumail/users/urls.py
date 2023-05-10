from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterNewUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', LogoutUser.as_view(), name='logout_user'),
    path('my_profile/<int:id>/', MyProfile.as_view(), name='my_profile'),
    path('my_profile/<int:id>/edit/', UpdateProfile.as_view(), name='update_profile'),
    path('my_profile/<int:pk>/edit/password/', NewPassword.as_view(), name='new_password'),
    path('my_profile/<int:pk>/subscriptions/', MySubscriptions.as_view(), name='my_subscriptions'),
    path('user/<int:pk>/', AnotherUser.as_view(), name='another_user'),
    path('user/<int:pk>/add_subscription/', add_subscription, name='add_subscription'),
    path('user/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
    path('search_users/', SearchUsers.as_view(), name='search_users'),
]
