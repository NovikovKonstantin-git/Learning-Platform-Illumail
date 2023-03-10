from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""Чтобы наша модель Profile автоматически обновлялась при создании/изменении данных модели User"""


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

#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instanse, **kwargs):
#     instanse.profile.save()





