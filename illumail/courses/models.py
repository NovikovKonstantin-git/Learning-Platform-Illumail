from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Courses(models.Model):
    CHOICES = [
        ('1', 'Публичный'),
        ('2', 'Платный'),
    ]


    title = models.CharField(max_length=300, verbose_name='Название')
    course_photo = models.ImageField(upload_to='courses_headers/%Y/%m/%d', default='dflt_crs_hdrs.jpg', verbose_name='Изображение курса')
    about_the_course = models.TextField(verbose_name='О курсе')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Автор курса', related_name='course')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    type_course = models.CharField(max_length=200, choices=CHOICES, default='1', verbose_name='Тип курса')
    price = models.IntegerField(verbose_name='Цена', blank=True, null=True)



    def get_absolute_url(self):
        return reverse('show_posts', kwargs={'course_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-time_created', ]


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')

    def get_absolute_url(self):
        return reverse('category_courses', kwargs={'category_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Posts(models.Model):
    CHOICES = [
        ('1', 'Лекция'),
        ('2', 'Практика'),
    ]
    title = models.CharField(max_length=300, verbose_name='Название')
    photo = models.ImageField(upload_to='posts_images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    file = models.FileField(upload_to='files/%Y/%m/%d', blank=True, verbose_name='Файл')
    post_text = models.TextField(verbose_name='Текст поста', blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменеия')
    post_type = models.CharField(max_length=200, choices=CHOICES, verbose_name='Тип поста')

    def get_absolute_url(self):
        return reverse('show_specific_post', kwargs={'course_id': self.course.id, 'post_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Материал курса'
        verbose_name_plural = 'Материалы курса'
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


class Comments(models.Model):
    comment_text = models.CharField(max_length=300, verbose_name='Текст комментария')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор комментария')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс с комментарием')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self):
        return f"{self.comment_text}"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-time_created']


class Quiz(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=300, verbose_name='Название теста')
    question = models.CharField(max_length=300, verbose_name='Вопрос')
    true_answer = models.CharField(max_length=300, verbose_name='Правильный ответ')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Тест с вписыванием ответа'
        verbose_name_plural = 'Тесты с вписыванием ответа'
        ordering = ['-time_created', ]


class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Тест')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    user_answer = models.CharField(max_length=300, verbose_name='Ответ пользователя')

    def __str__(self):
        return f"{self.quiz}"

    class Meta:
        verbose_name = 'Ответ на тест в вписыванем'
        verbose_name_plural = 'Ответы на тест в вписыванем'


class Testing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Question(models.Model):
    test = models.ForeignKey(Testing, on_delete=models.CASCADE)
    text = models.TextField()


class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)


class GoodTestModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название теста')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class QuestionModel(models.Model):
    test = models.ForeignKey(GoodTestModel, on_delete=models.CASCADE, verbose_name='Название теста')
    question = models.CharField(max_length=500, verbose_name='Вопрос')
    true_answer = models.CharField(max_length=500, verbose_name='Правильный ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, verbose_name='Вопрос')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    user_answer = models.CharField(max_length=300, verbose_name='Ответ пользователя')

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = 'Ответ на тест'
        verbose_name_plural = 'Ответы на тест'


class Progress(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    progress = models.IntegerField(validators=[MaxValueValidator(limit_value=100), ], default=0, verbose_name='Прогресс')

    def __str__(self):
        return f"{self.progress}"

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'