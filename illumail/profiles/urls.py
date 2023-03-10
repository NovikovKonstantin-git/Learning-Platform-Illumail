from django.urls import path, include
from .views import *
from .forms import *

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),

]