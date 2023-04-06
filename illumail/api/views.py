from rest_framework import generics
from .serializers import CoursesSerializer
from courses.models import Courses


class CoursesApiView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
