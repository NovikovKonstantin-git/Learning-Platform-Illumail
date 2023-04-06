from rest_framework import generics
from .serializers import CoursesSerializer
from courses.models import Courses


class CoursesAPIList(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CoursesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class CoursesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
