from django import forms
from .models import CompletedTaskModel, Courses, Posts, Comments


class ComplitedTaskForm(forms.ModelForm):
    file = forms.FileField(label='Файл', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = CompletedTaskModel
        fields = ['file', ]


class CreateOrUpdateCourseForm(forms.ModelForm):
    about_the_course = forms.CharField(widget=forms.Textarea(attrs={'cols': 85, 'rows': 15}))
    type_course = forms.ChoiceField(choices=Courses.CHOICES, widget=forms.RadioSelect(), required=True)

    class Meta:
        model = Courses
        fields = ['title', 'course_photo', 'about_the_course', 'category', 'type_course', 'price']


class CreateOrUpdatePostForm(forms.ModelForm):
    post_type = forms.ChoiceField(choices=Posts.CHOICES, widget=forms.RadioSelect(), required=True, label='Тип задания')

    class Meta:
        model = Posts
        fields = ['title', 'photo', 'file', 'post_text', 'post_type']


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label='Текст комментария', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Comments
        fields = ['comment_text', ]
