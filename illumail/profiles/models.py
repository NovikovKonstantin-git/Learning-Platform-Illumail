from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Расскажите о себе...", max_length=300)
    email = models.EmailField(max_length=200, unique=True, blank=True)
    avatar = models.ImageField(default="avatar.png", upload_to='avatars/%Y/%m/%d')
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}-{self.time_created}"

