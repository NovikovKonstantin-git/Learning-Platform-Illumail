from django.urls import path, include
from .views import *

urlpatterns = [
    path('courses/', show_courses, name='show_courses'),
    path('courses/<int:course_id>/posts/', show_posts, name='show_posts'),
    path('courses/<int:course_id>/posts/<int:post_id>/', show_specific_post, name='show_specific_post'),
]
