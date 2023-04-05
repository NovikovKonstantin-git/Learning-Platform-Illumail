from django.contrib.auth import get_user_model
from rest_framework import serializers
from courses.models import Courses


class CoursesSerializer(serializers.ModelSerializer):
    time_created = serializers.ReadOnlyField()
    time_updated = serializers.Serializer()

    class Meta:
        model = Courses
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'username')