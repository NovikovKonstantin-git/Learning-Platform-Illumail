from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', show_courses, name='show_courses'),
    path('courses/<int:course_id>/posts/', show_posts, name='show_posts'),
    path('courses/<int:course_id>/posts/<int:post_id>/', show_specific_post, name='show_specific_post'),
    path('courses/create/', create_course, name='create_course'),
    path('courses/<int:id>/update/', update_course, name='update_course'),
    path('course/<int:id>/delete/', delete_course, name='delete_course'),
]
