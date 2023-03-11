from django.urls import path, include
from .views import *
from .forms import *

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user'),
    path('my_profile/<int:user_id>', my_profile, name='my_profile'),
]
