from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

from users.models import CustomUser


class StudyGroup(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    group_photo = models.ImageField(upload_to='groups_headers/%Y/%m/%d', default='dflt_crs_hdrs.jpg',
                                    verbose_name='Изображение группы')
    about_the_group = models.TextField(verbose_name='О группе')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Автор группы',
                               related_name='study_groups')

    def get_absolute_url(self):
        return reverse('show_posts_group', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ['-time_created', ]


class PostsInStudyGroup(models.Model):
    CHOICES = [
        ('1', 'Лекция'),
        ('2', 'Практика'),
    ]
    title = models.CharField(max_length=300, verbose_name='Название')
    photo = models.ImageField(upload_to='posts_images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл')
    post_text = models.TextField(verbose_name='Текст поста', blank=True)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, verbose_name='Учебная группа')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменеия')
    post_type = models.CharField(max_length=200, choices=CHOICES, verbose_name='Тип поста')

    def get_absolute_url(self):
        return reverse('show_specific_task', kwargs={'pk': self.study_group.id, 'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал группы'
        verbose_name_plural = 'Метериалы группы'
        ordering = ['-time_created', ]


class CompletedTaskInStudyGroup(models.Model):
    file = models.FileField(upload_to='compl_tasks/%Y/%m/%d', blank=True, verbose_name='Файл')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(PostsInStudyGroup, on_delete=models.CASCADE, verbose_name='Задание')
    time_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    grade = models.IntegerField(validators=[MaxValueValidator(limit_value=10), ], verbose_name='Оценка')

    def __str__(self):
        return f"{self.file}"

    class Meta:
        verbose_name = 'Выполненное задание'
        verbose_name_plural = 'Выполненные задания'
        ordering = ['-time_load', ]



















class Valuation(models.Model):
    post_task = models.ForeignKey(PostsInStudyGroup, on_delete=models.PROTECT, verbose_name='Задание')
    compl_task = models.ForeignKey(CompletedTaskInStudyGroup, on_delete=models.PROTECT,
                                   verbose_name='Выполненное задание', related_name='valuations')
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Учащийся')
    valuation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оценивания')
    grade = models.IntegerField(validators=[MaxValueValidator(limit_value=10), ], verbose_name='Оценка')

    def __str__(self):
        return f"{self.user}-{self.post_task}"

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
