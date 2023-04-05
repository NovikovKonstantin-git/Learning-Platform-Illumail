from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Courses(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    course_photo = models.ImageField(upload_to='courses_headers/%Y/%m/%d', blank=True, verbose_name='Изображение курса')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Автор курса')

    def get_absolute_url(self):
        return reverse('show_posts', kwargs={'course_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['title', ]


class Posts(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    photo = models.ImageField(upload_to='posts_images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл')
    post_text = models.TextField(verbose_name='Текст поста', blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменеия')

    def get_absolute_url(self):
        return reverse('show_specific_post', kwargs={'course_id': self.course.id, 'post_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_created', ]


class CompletedTaskModel(models.Model):
    file = models.FileField(upload_to='compl_tasks/%Y/%m/%d', blank=True, verbose_name='Файл')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Пост')
    time_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return f"{self.file}"

    class Meta:
        verbose_name = 'Выполненное задание'
        verbose_name_plural = 'Выполненные задания'
        ordering = ['-time_load', ]