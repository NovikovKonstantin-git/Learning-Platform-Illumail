from django.template.context_processors import request
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CoursesSerializer, UserSerializer, CreateUserSerializer
from courses.models import Courses
from users.models import CustomUser
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthorOrReadOnly, ]


class MyProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return CustomUser.objects.all()
        # return CustomUser.objects.filter(pk=self.request.user.id)

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]


class UserAPICreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

