from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d', verbose_name='Фото', blank=True)
    bio = models.CharField(max_length=200, verbose_name='О себе', blank=True)
    patronymic = models.CharField(max_length=300, verbose_name='Отчество')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def get_absolute_url(self):
        return reverse('my_profile', kwargs={'id': self.id})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
