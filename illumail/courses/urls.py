from django.urls import path
from .views import *

urlpatterns = [
    path('', redirectik, name='redirectik'),
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
    path('courses/<int:pk>/posts/create_test/', CreateTest.as_view(), name='create_test'),
    path('courses/<int:pk>/posts/test/<int:test_id>/', ShowSpecificTest.as_view(), name='show_specific_test'),
    path('courses/sort/', SortCourses.as_view(), name='sort_courses'),
    path('courses/filter/', FilterCourses.as_view(), name='filter_courses'),
    path('courses/new_test/', create_test, name='new_test'),

    path('course/<int:course_id>/test/<int:pk>/', GoodTest.as_view(), name='good_test'),
    # path('course/<int:course_id>/test/<int:pk>/questions/<int:question_id>/save/', save_user_answer, name='save_user_answer'),
    path('course/<int:pk>/test/questions/<int:question_id>/save/', save_user_answer, name='save_user_answer'),
]
