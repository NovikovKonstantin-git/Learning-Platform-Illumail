from django import forms
from .models import CompletedTaskInStudyGroup, StudyGroup, PostsInStudyGroup


class ComplitedTaskGroupForm(forms.ModelForm):
    file = forms.FileField(label='Файл', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = CompletedTaskInStudyGroup
        fields = ['file', ]


class CreateOrUpdateGroupForm(forms.ModelForm):
    about_the_group = forms.CharField(widget=forms.Textarea(attrs={'cols': 85, 'rows': 15}))

    class Meta:
        model = StudyGroup
        fields = ['title', 'group_photo', 'about_the_group']


class CreateOrUpdatePostForm(forms.ModelForm):
    post_type = forms.ChoiceField(choices=PostsInStudyGroup.CHOICES, widget=forms.RadioSelect(), required=True, label='Тип задания')

    class Meta:
        model = PostsInStudyGroup
        fields = ['title', 'photo', 'file', 'post_text', 'post_type']