from django.shortcuts import render
from rest_framework import generics
from users.forms import CustomUser
from .serializers import UserSerializer
from . import serializers
from courses.models import Courses


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class CoursesList(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = serializers.CoursesSerializer


class CoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = serializers.CoursesSerializer