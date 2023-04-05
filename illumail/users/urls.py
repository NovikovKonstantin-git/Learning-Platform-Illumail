from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('my_profile/<int:id>/', my_profile, name='my_profile'),
    path('my_profile/<int:id>/edit/', update_profile, name='update_profile')
]