from django.urls import path
from .views import *


urlpatterns = [
    path('study_group/<int:pk>/posts/', ShowPostsGroups.as_view(), name='show_posts_group'),
    path('study_group/<int:pk>/posts/<int:post_id>/', show_specific_task, name='show_specific_task'),
    path('study_group/<int:pk>/tasks/<int:post_id>/delete/', delete_task, name='delete_task'),
]
