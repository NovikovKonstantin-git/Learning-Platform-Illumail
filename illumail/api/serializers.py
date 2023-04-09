from django.contrib.auth import get_user_model
from rest_framework import serializers
from courses.models import Courses


class CoursesSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Courses
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic', 'photo', 'email', 'username', 'bio', 'password',
                  'time_created', 'time_updated']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic', 'email', 'username', 'password', 'time_created',
                  'time_updated']

