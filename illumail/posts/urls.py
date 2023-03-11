from django.urls import path, include
from .views import *

urlpatterns = [
    path('courses/', show_all_courses, name='show_all_courses'),
    path('courses/<int:course_id>/posts/', show_posts, name='show_posts'),
    path('courses/<int:course_id>/posts/<int:post_id>/', show_specific_task, name='show_specific_task'),
    path('course/add_course/', create_course, name='create_course'),
    path('course/join/', join_the_course, name='join_the_course')
]