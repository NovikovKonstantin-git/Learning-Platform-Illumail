from django import forms
from .models import CompletedTaskModel, Courses


class ComplitedTaskForm(forms.ModelForm):
    file = forms.FileField(label='Файл', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = CompletedTaskModel
        fields = ['file', ]


class CreateOrUpdateCourseForm(forms.ModelForm):
    about_the_course = forms.CharField(widget=forms.Textarea(attrs={'cols': 85, 'rows': 15}))

    class Meta:
        model = Courses
        fields = ['title', 'course_photo', 'about_the_course']
