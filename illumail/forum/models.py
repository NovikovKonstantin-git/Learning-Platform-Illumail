from django.db import models
from users.models import CustomUser


class ForumSection(models.Model):
    section = models.CharField(max_length=300, verbose_name='Раздел')

    def __str__(self):
        return f"{self.section}"

    class Meta:
        verbose_name = 'Раздел форума'
        verbose_name_plural = 'Разделы форума'


class ForumSubsection(models.Model):
    subsection = models.CharField(max_length=300, verbose_name='Тема')
    section = models.ForeignKey(ForumSection, on_delete=models.CASCADE, verbose_name='Раздел')

    def __str__(self):
        return f"{self.subsection}"

    class Meta:
        verbose_name = 'Тема форума'
        verbose_name_plural = 'Темы форума'


class ForumCommunication(models.Model):
    subsection = models.ForeignKey(ForumSubsection, on_delete=models.CASCADE, verbose_name='Тема')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Пользователь')
    comm_text = models.TextField(verbose_name='Текст')
    date_text = models.DateField(auto_now=True, verbose_name='Дата сообщения')

    def __str__(self):
        return f"{self.subsection}"

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        ordering = ['-date_text', ]


