from django.urls import path
from .views import *
from rest_framework import routers


urlpatterns = [
    path('api/courses/', CoursesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/courses/<int:pk>/', CoursesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/users/<int:pk>/my_profile/', MyProfileAPI.as_view()),
    path('api/users/create/', UserAPICreate.as_view()),
]


