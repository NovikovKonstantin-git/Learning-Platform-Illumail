from django.urls import path, include
from forum.views import *


urlpatterns = [
    path('forum/', ShowSection.as_view(), name='show_section'),
    path('forum/section/<int:pk>', ShowSubsections.as_view(), name='show_subsections'),
    path('forum/section/<int:pk>/communication/', ShowCommunication.as_view(), name='show_communication'),
]