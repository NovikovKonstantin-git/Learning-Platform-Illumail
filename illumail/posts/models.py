from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, verbose_name='Курс', null=True)

    def get_absolute_url(self):
        return reverse('show_specific_task', kwargs={"course_id": self.course.id, "post_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['time_create', ]


class Courses(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    photo = models.ImageField(upload_to='courses_header_image/%Y/%m/%d/', blank=True, verbose_name='Изображение курса', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['time_create', ]

