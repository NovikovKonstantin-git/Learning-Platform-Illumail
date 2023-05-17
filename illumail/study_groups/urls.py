from django.urls import path, include
from .views import *


urlpatterns = [
    path('study_group/<int:pk>/posts/', ShowPostsGroups.as_view(), name='show_posts_group'),
    path('study_group/<int:pk>/posts/<int:post_id>/', show_specific_task, name='show_specific_task'),
    path('study_group/<int:pk>/tasks/<int:post_id>/delete/', delete_task, name='delete_task'),
    path('study_group/create/', CreateGroup.as_view(), name='create_group'),
    path('study_group/<int:pk>/update/', UpdateGroup.as_view(), name='update_group'),
    path('study_group/<int:pk>/delete/', delete_group, name='delete_group'),
    path('study_group/<int:study_group_id>/posts/create/', CreateTask.as_view(), name='create_task'),
    path('study_group/<int:pk>/students', ShowStudents.as_view(), name='show_students'),
]
