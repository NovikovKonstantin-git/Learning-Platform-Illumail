from django import forms
from .models import *


class ComplitedTaskForm(forms.ModelForm):
    # file = forms.FileField(label='Файл', widget=forms.ClearableFileInput(attrs={'multiple': True}))
    file = forms.FileField(label='Файл')

    class Meta:
        model = CompletedTaskModel
        fields = ['file', ]


class CreateOrUpdateCourseForm(forms.ModelForm):
    about_the_course = forms.CharField(widget=forms.Textarea(attrs={'cols': 85, 'rows': 15}))

    class Meta:
        model = Courses
        fields = ['title', 'course_photo', 'about_the_course', 'category', 'price']


class CreateOrUpdatePostForm(forms.ModelForm):
    # post_type = forms.ChoiceField(choices=Posts.CHOICES, widget=forms.RadioSelect(), required=True, label='Тип задания')

    class Meta:
        model = Posts
        fields = ['title', 'photo', 'file', 'post_text']


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label='Текст комментария', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Comments
        fields = ['comment_text', ]


class CreateTestForm(forms.ModelForm):
    title = forms.CharField(label='Название теста', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    question = forms.CharField(label='Вопрос', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    true_answer = forms.CharField(label='Правильный ответ', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Quiz
        fields = ['title', 'question', 'true_answer']


class AnswerForm(forms.ModelForm):
    user_answer = forms.CharField(label='Ответ на вопрос', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Answer
        fields = ['user_answer', ]


class TestingForm(forms.ModelForm):
    class Meta:
        model = Testing
        fields = ['name', 'description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text', 'is_correct']


"""Новое"""


class GoodAnswerForm(forms.ModelForm):
    user_answer = forms.CharField(label='Ответ на вопрос', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = AnswerModel
        fields = ['user_answer', ]