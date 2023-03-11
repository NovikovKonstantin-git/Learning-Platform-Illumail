from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(default="Расскажите о себе...", max_length=300, verbose_name='О себе')
    avatar = models.ImageField(default="avatar.png", upload_to='avatars/%Y/%m/%d', verbose_name='Фото')
    followers = models.ManyToManyField(User, blank=True, related_name='followers', verbose_name='Фолловеры')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['time_created', ]



