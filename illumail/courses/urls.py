from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', ShowCourses.as_view(), name='show_courses'),
    path('courses/<int:course_id>/posts/', ShowPosts.as_view(), name='show_posts'),
    path('courses/<int:course_id>/posts/<int:post_id>/', show_specific_post, name='show_specific_post'),
    path('courses/create/', CreateCourse.as_view(), name='create_course'),
    path('courses/<int:pk>/update/', UpdateCourse.as_view(), name='update_course'),
    path('courses/<int:pk>/delete/', delete_course, name='delete_course'),
    path('courses/search/', SearchCourse.as_view(), name='search_course'),
    path('courses/teaching/', Teaching.as_view(), name='teaching'),
    path('courses/category/<int:category_id>/', category_courses, name='category_courses'),
    path('learning/', Learning.as_view(), name='learning'),
    path('leave_the_course/<int:pk>/', leave_the_course, name='leave_the_course'),
    path('join_the_course/<int:pk>/', join_the_course, name='join_the_course'),
    path('news/', ShowNews.as_view(), name='show_news'),
    path('courses/<int:course_id>/posts/create/', CreatePost.as_view(), name='create_post'),
    path('courses/<int:pk>/posts/<int:post_id>/delete/', delete_post, name='delete_post'),
    # Study Group
]
