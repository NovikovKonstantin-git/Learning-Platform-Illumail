from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('api/users/', views.UserList.as_view()),
    path('api/users//', views.UserDetail.as_view()),
    path('api/courses/', views.CoursesList.as_view()),
    path('api/courses//', views.CoursesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

