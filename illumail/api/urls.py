from django.urls import path
from .views import *


urlpatterns = [
    path('api/courses/', CoursesAPIList.as_view()),
    path('api/courses/<int:pk>/update/', CoursesAPIUpdate.as_view()),
    path('api/courses/<int:pk>/delete/', CoursesAPIDestroy.as_view()),
]

