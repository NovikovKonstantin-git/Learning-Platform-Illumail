from django.urls import path
from .views import *


urlpatterns = [
    path('api/courses/', CoursesApiView.as_view()),
]
